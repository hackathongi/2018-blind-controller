# -*- coding: utf-8 -*-
import logging
import requests
from json import dumps, loads


logger = logging.getLogger('RequestSender')

ORION_SERVER_PRIVATE = '192.168.4.230'
ORION_SERVER_PUBLIC = '84.89.60.4'
ORION_PORT = 80
BASE_URL = 'http://{server}:{port}/'
MY_UNIQUE_ID = 'persiana'
MY_TYPE = 'blind_controller'
HEADERS={'Content-Type': 'application/json'}


def registerSubscriptions(private=False):
    logger.info('Subscripting to house monitor')
    server = ORION_SERVER_PRIVATE if private else ORION_SERVER_PUBLIC
    url = BASE_URL.format(server=server, port=ORION_PORT) + 'v2/subscriptions'
    json_vals = {
        "description": "Subscripció de luminositat per activar la persiana",
        "subject": {
            "entities": [
                {
                    "id": "sensors",
                    "type": "sensors"
                }
            ],
            "condition": {
                "attrs": [
                    "estat"
                ]
            }
        },
        "notification": {
            "http": {
                "url": "http://192.168.4.13"  # Persianes
            },
            "attrs": [
                "fotoresistencia",
                "temperatura"
            ]
        },
        "expires": "2040-01-01T14:00:00.00Z",
        "throttling": 1
    }
    response = requests.post(url=url, json=json_vals, headers=HEADERS)
    if response.status_code >= 400:
        logger.error('Failed to subscribe')
        logger.error(response.content)
    return response.status_code


def updateServerInfo(element, private=True):
    logger.info('Updating Server Info')
    server = ORION_SERVER_PRIVATE if private else ORION_SERVER_PUBLIC
    url = BASE_URL.format(server=server, port=ORION_PORT) + 'v2/entities/'
    url += MY_UNIQUE_ID + '/attrs'
    json_vals = {
        'state': {
            'value': (
                'opening' if element.engine_state else (
                    'closing' if element.engine_state == -1 else 'stopped'
                )
            ),
            'type': 'String'
        },
        'percentage': {
            'value': str(element.rotation_point/element.max),
            'type': 'String'
        },
        'mode': {
            'value': 'manual',
            'type': 'String'
        },
    }
    response = requests.post(
        url=url, json=json_vals, headers=HEADERS
    )
    if response.status_code >= 400:
        logger.error('Failed to update status')
        logger.error(response.content)
        return False
    return True


def getServerVersion(private=True):
    logger.info('Requesting Server Version')
    server = ORION_SERVER_PRIVATE if private else ORION_SERVER_PUBLIC
    url = BASE_URL.format(server=server, port=ORION_PORT) + 'version'
    response = requests.get(url)
    if response.status_code != 200:
        logger.error('Failed to Get Server Version!')
        logger.error(str(response.content))
        return response.status_code
    data = loads(response.content)['orion']
    logger.info('Version: {}'.format(data['version']))
    logger.info('Uptime: {}'.format(data['uptime']))
    return response.status_code
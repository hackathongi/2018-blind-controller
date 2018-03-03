# -*- coding: utf-8 -*-
import logging
import requests


logger = logging.getLogger('RequestSender')

ORION_SERVER_PRIVATE = '192.168.4.230'
ORION_SERVER_PUBLIC = '84.89.60.4'
ORION_PORT = 80
BASE_URL = 'http://{server}:{port}/'


def registerEntity():
    logger.info('Requesting Entity Register')
    return True


def getServerVersion(private=False):
    logger.info('Requesting Server Version')
    server = ORION_SERVER_PRIVATE if private else ORION_SERVER_PUBLIC
    url = BASE_URL.format(server=server, port=ORION_PORT)
    response = requests.get(url)
    if response.status_code != 200:
        logger.error('Failed to Get Server Version!')
        logger.error(str(response.content))
        return response.status_code
    data = response.content['orion']
    logger.info('Version: {}'.format(data['version']))
    logger.info('Uptime: {}'.format(data['uptime']))
    return response.status_code
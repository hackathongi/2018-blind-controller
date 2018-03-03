# -*- coding: utf-8 -*-
import logging


logger = logging.getLogger('RequestSender')

ORION_SERVER_PRIVATE = '192.168.4.230'
ORION_SERVER_PUBLIC = '84.89.60.4'
ORION_PORT = 80


def registerEntity():
    logger.info('Requesting Entity Register')
    return True


def getServerVersion():
    logger.info('Requesting Server Version')
    return True
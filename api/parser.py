# -*- coding: utf-8 -*-

import logging


logger = logging.getLogger('RequestParser')


def parse_request(request_data):
    logger.info('Parsing request')
    return request_data
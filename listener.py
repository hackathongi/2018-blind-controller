# -*- coding: utf-8 -*-
from core.core import Core
from flask import request
from api import sender
from json import loads
import logging
import click
import flask


app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def subscription():
    data = loads(request.data)
    for sub in data['data']:
        if sub['id'] == 'sensors':
            house_core.update_sensors(light_lvl=sub['fotoresistencia']['value'])
        elif sub['id'] == sender.MY_UNIQUE_ID:
            action = sub['action']['value']
            if action == 'baixa':
                house_core.blind_down()
            elif action == 'puja':
                house_core.blind_up()
            elif action == 'para':
                house_core.blind_stop()
            else:
                return 'ERROR, ACTION NOT DEFINED', 500
        else:
            return 'ERROR, SUBSCRIPTION NOT ALLOWED', 500
    return 'OK', 200


@app.route('/pujar', methods=['POST'])
def pujar_persiana():
    logger = logging.getLogger('Flaskapp')
    logger.info('Pujant')
    house_core.blind_up(t=12)
    return 'OK', 200


@app.route('/parar', methods=['POST'])
def parar_persiana():
    logger = logging.getLogger('Flaskapp')
    logger.info('Parant')
    house_core.blind_stop()
    return 'OK', 200


@app.route('/baixar', methods=['POST'])
def baixar_persiana():
    logger = logging.getLogger('Flaskapp')
    logger.info('Baixant')
    house_core.blind_down(t=10)
    return 'OK', 200


@click.command()
@click.option('-v', '--verbosity', is_flag=True, help='Show verbose output')
@click.option('-p', '--port', default=80, type=int, help='Port to listen on')
@click.option(
    '-i', '--interface', default='0.0.0.0', type=str, help='Interface to bind')
def startup(verbosity, port, interface):
    logging.basicConfig(
        format='[%(asctime)s][%(levelname)s]%(name)s: %(message)s',
        datefmt='%Y/%m/%d-%H:%M:%S',
        level=logging.INFO if verbosity else logging.WARNING
    )
    global house_core
    house_core = Core()
    if sender.getServerVersion() >= 400:
        exit(-1)
    # if sender.registerSubscriptions() >= 400:
    #     exit(-1)
    app.run(host=interface, port=port)


if __name__ == '__main__':
    startup()

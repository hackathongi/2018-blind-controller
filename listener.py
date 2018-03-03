# -*- coding: utf-8 -*-
from core.core import Core
from api import sender
import logging
import click
import flask


app = flask.Flask(__name__)


@app.route('/pujar', methods=['POST', 'OPTIONS'])
def pujar_persiana():
    logger = logging.getLogger('Flaskapp')
    logger.info('Pujant')
    house_core.blind_up(t=12)
    return 'OK', 200


@app.route('/parar', methods=['POST', 'OPTIONS'])
def parar_persiana():
    logger = logging.getLogger('Flaskapp')
    logger.info('Parant')
    house_core.blind_stop()
    return 'OK', 200


@app.route('/baixar', methods=['POST', 'OPTIONS'])
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

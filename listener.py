import logging
import click
import flask

app = flask.Flask(__name__)


@app.route('/')
def default():
    print('OK')


@click.command()
@click.option('-v', '--verbosity', help='Show verbose output')
@click.option('-p', '--port', type=int, help='Port to listen on')
@click.option('-i', '--interface', type=str, help='Interface to bind')
def startup(verbosity, port, interface):
    logging.basicConfig(format='[%(asctime)s]%(name)s: %(message)s',
                        datefmt='%Y/%m/%d-%H:%M:%S',
                        level=logging.INFO if verbosity else logging.WARNING)
    app.run(host=interface, port=port)


if __name__ == '__main__':
    startup()
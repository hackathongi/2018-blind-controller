import click
import RPi.GPIO as GPIO


@click.command()
def blind_stop():
    print("Stop blind")
    GPIO.cleanup()


if __name__ == '__main__':
    blind_stop()

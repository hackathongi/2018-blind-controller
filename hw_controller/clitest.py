import click
import RPi.GPIO as GPIO
import time


@click.command()
def testing_mode():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.IN)
    try:
        while True:
            i = GPIO.input(13)
            print("Sensor value: "+i)
            time.sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    testing_mode()

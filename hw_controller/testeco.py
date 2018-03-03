import click
import RPi.GPIO as GPIO
import time


@click.command()
def testeco():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.IN)
        while True:
            GPIO.output(13, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(13, GPIO.HIGH)
            time.sleep(0.5)
            i = GPIO.input(15)
            GPIO.output(13, GPIO.LOW)
            print("Val: "+str(i))
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    testeco()
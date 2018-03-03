import click
import RPi.GPIO as GPIO
import time


@click.command()
def blind_close():
    print("Closing blind")
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        pwm = GPIO.PWM(11, 50)
        pwm.start(5)
        pwm.ChangeDutyCycle(12)
        while True:
            pass
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    blind_close()

import click
import RPi.GPIO as GPIO


@click.command()
def blind_open():
    print("Open blind")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    pwm = GPIO.PWM(11, 50)
    pwm.start(5)
    pwm.ChangeDutyCycle(2)


if __name__ == '__main__':
    blind_open()

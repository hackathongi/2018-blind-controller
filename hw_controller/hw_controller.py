import RPi.GPIO as GPIO
import time


def blind_open(t=0):
    print("Start opening blind")
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.IN)
        GPIO.setwarnings(False)
        pwm = GPIO.PWM(11, 50)
        pwm.start(5)
        pwm.ChangeDutyCycle(2)
        while GPIO.input(13) != 0:
            pass
    finally:
        print("Stop opening blind")
        GPIO.cleanup()


def blind_close(t=0):
    print("Start closing blind")
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(15, GPIO.IN)
        GPIO.setwarnings(False)
        pwm = GPIO.PWM(11, 50)
        pwm.start(5)
        pwm.ChangeDutyCycle(12)
        print("Val: ")
        print(GPIO.input(15))
        while int(GPIO.input(15)) != 1:
            pass
    finally:
        print()
        GPIO.cleanup()

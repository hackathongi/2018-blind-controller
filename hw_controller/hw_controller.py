import RPi.GPIO as GPIO
import time


def blind_open(t=0):
    print("Opening blind")
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        pwm = GPIO.PWM(11, 50)
        pwm.start(5)
        pwm.ChangeDutyCycle(2)
        if t == 0:
            while True:
                pass
        else:
            time.sleep(t)
    finally:
        GPIO.cleanup()


def blind_close(t=0):
    print("Closing blind")
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        pwm = GPIO.PWM(11, 50)
        pwm.start(5)
        pwm.ChangeDutyCycle(12)
        if t == 0:
            while True:
                pass
        else:
            time.sleep(t)
    finally:
        GPIO.cleanup()

import RPi.GPIO as GPIO
import time


def blind_open(t=0):
    print("Start opening blind")
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
        print("Stop opening blind")
        GPIO.cleanup()


def blind_close(t=0):
    print("Start closing blind")
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
        print("Stop closing blind")
        GPIO.cleanup()

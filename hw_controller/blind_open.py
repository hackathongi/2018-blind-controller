import click
import RPi.GPIO as GPIO
import time

@click.command()
@click.option('--elem_id', type=int, help="Objective  HW element id")
@click.option('--dir', type=int, help="Objective  HW element id")
def open_blind(elem_id,dir):

    if (elem_id == 1):
        print("Servo Mode!")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        pwm = GPIO.PWM(11, 50)
        pwm.start(5)
        try:
            while True:  # iniciamos un loop infinito
                if dir == 1:
                    pwm.ChangeDutyCycle(2)
                elif dir == 2:
                    pwm.ChangeDutyCycle(12)
        except KeyboardInterrupt:  # Si el usuario pulsa CONTROL+C entonces...
            GPIO.cleanup()  # Limpiamos los pines GPIO de la Raspberry y cerramos el script
    elif (elem_id == 2):
        print("LED MODE")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        try:
            while True:  # iniciamos un loop infinito
                GPIO.output(18, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(18, GPIO.LOW)
                time.sleep(1)
        except KeyboardInterrupt:  # Si el usuario pulsa CONTROL+C entonces...
            GPIO.cleanup()  # Limpiamos los pines GPIO de la Raspberry y cerramos el script

if __name__ == '__main__':
    open_blind()
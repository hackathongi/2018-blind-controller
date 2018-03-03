import click
import RPi.GPIO as GPIO
import time

@click.command()
@click.option('--elem_id', type=int, help="Objective  HW element id")
def open_blind(elem_id):

    if (elem_id == 1):
        GPIO.setmode(GPIO.BOARD)  # Ponemos la Raspberry en modo BOARD
        GPIO.setup(21, GPIO.OUT)  # Ponemos el pin 21 como salida
        p = GPIO.PWM(21, 50)  # Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
        p.start(7.5)  # Enviamos un pulso del 7.5% para centrar el servo

        try:
            while True:  # iniciamos un loop infinito

                p.ChangeDutyCycle(4.5)  # Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
                time.sleep(0.5)  # pausa de medio segundo
                p.ChangeDutyCycle(10.5)  # Enviamos un pulso del 10.5% para girar el servo hacia la derecha
                time.sleep(0.5)  # pausa de medio segundo
                p.ChangeDutyCycle(7.5)  # Enviamos un pulso del 7.5% para centrar el servo de nuevo
                time.sleep(0.5)  # pausa de medio segundo

        except KeyboardInterrupt:  # Si el usuario pulsa CONTROL+C entonces...
            p.stop()  # Detenemos el servo
            GPIO.cleanup()  # Limpiamos los pines GPIO de la Raspberry y cerramos el script
    elif (elem_id == 2):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        print "LED on"
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        print "LED off"
        GPIO.output(18, GPIO.LOW)
        GPIO.cleanup()

if __name__ == '__main__':
    open_blind()
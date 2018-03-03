import click
import RPi.GPIO as GPIO
import time

@click.command()
@click.option('--elem_id', type=int, help="Objective  HW element id")
def open_blind(elem_id):

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


if __name__ == '__main__':
    open_blind()
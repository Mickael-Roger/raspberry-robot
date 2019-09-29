import RPi.GPIO as GPIO          
from time import sleep
import signal



in1 = 11
in2 = 12
en = 13
temp1=1

in3 = 15
in4 = 16
enb = 18

IRdevant = 40

def fin():
    GPIO.cleanup()

def start():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IRdevant, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.setup(enb,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)



def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def avance(nb):

    for i in range(0, nb * 3):
        if GPIO.input(IRdevant) == 0:
            stop()
        else:
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)

        sleep(0.01)

    stop()

def recule(nb):

    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    sleep(0.1 * nb)

    stop()

def droite(nb):

    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    sleep(0.089 * nb)

    stop()

def gauche(nb):

    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    sleep(0.089 * nb)

    stop()

def handler(signum, frame):
    fin()

start()

p=GPIO.PWM(en,1000)
q=GPIO.PWM(enb,1000)
p.start(25)
q.start(25)

p.ChangeDutyCycle(100)
q.ChangeDutyCycle(100)


signal.signal(signal.SIGINT, handler)

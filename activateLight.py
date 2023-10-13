import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

led=6
GPIO.setup(led,GPIO.OUT)

GPIO.output(led, GPIO.LOW)
pwm = GPIO.PWM(led,50)
pwm.start(0)

def run(state):
        bright=50
        if state == 1:
                for bright in range(bright,0,-5):
                        pwm.ChangeDutyCycle(bright)
                        time.sleep(0.05)
        elif state == 0:
                for bright in range(bright,100,5):
                        pwm.ChangeDutyCycle(bright)
                        time.sleep(0.05)
        else:
                pwm.ChangeDutyCycle(bright)

from gpiozero import Motor
import time

motor = Motor(forward=5, backward=26)
def run(state):
        if state == 1:
            motor.forward(speed = 0.5)
        else:
                motor.forward(speed = 0)

import serial
import time

port = "/dev/ttyACM0"
serial = serial.Serial(port, 9600)

on = "1"
off = "0"

def run(state):
        if(state == 1):
                serial.write(on.encode())
        else:
                serial.write(off.encode()

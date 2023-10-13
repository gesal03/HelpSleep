import time
import RPi.GPIO as GPIO
trig = 20
echo = 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)
def measureDistance():
        global trig, echo
        time.sleep(0.5)
        GPIO.output(trig, True) # 신호 1
        #time.sleep(0.00001) # 짧은 시간을 나타내기 위함
        GPIO.output(trig, False) # 신호가 1-> 0으로 떨어질 때 초음파발생
        while(GPIO.input(echo) == 0):
            pass
        pulse_start = time.time() # echo 신호가 1인 경우, 초음파 발사된 순간
        while(GPIO.input(echo) == 1):
                pass
        pulse_end = time.time() # 초음파 신호가 도착한 순간
        pulse_duration = pulse_end - pulse_start
        return 340*100/2*pulse_duration

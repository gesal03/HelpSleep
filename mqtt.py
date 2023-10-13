# publisher

import time
import paho.mqtt.client as mqtt
import checkDistance # 초음파 센서 입력 모듈 임포트
import checkHumidity
import checkTemperature
import checkBright
import activateHumidifier
import activateLight
import activateMotor
import activateAlert

broker_ip = "localhost" # 현재 이 컴퓨터를 브로커로 설정

client = mqtt.Client()
client.connect(broker_ip, 1883)
client.loop_start()

while(True):
        distance = checkDistance.measureDistance()
        if distance < 6:
                activateAlert.run(1)
                client.publish("alert", "경고음이 울렸습니다.", qos=0)
        else:
                activateAlert.run(0)
        client.publish("distance", distance, qos=0)

        humidity = checkHumidity.getHumidity()
        if(humidity < 90):
                activateHumidifier.run(1)
        else:
                client.publish("humidifier","가습기가 꺼졌습니다.", qos=0)
                activateHumidifier.run(0)
        client.publish("humidity", humidity, qos=0)

        temperature = checkTemperature.getTemperature()
        if(temperature > 24):
                client.publish("motor","선풍기가 켜졌습니다.", qos=0)
                activateMotor.run(1)
        else:
                activateMotor.run(0)
        client.publish("temperature", temperature, qos=0)

        bright = checkBright.getBright()
        if(bright > 70):
                client.publish("light","무드등의 밝기를 키웁니다.", qos=0)
                activateLight.run(0)
        elif(bright < 30):
                client.publish("light","무드등의 밝기를 줄입니다.", qos=0)
                activateLight.run(1)
        else:
                activateLight.run(2)

        client.publish("bright", bright, qos=0)
        time.sleep(5)

client.loop_stop()
client.disconnect()

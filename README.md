# HelpSleep
😪 2022 모바일&amp;스마트시스템 Mini Project - 수면 보조 시스템

## 설명
편안한 숙면을 도와주는 시스템이다. 숙면에는 온도, 습도, 조도가 중요하다. <br>
이에 따라 사용자가 수면을 취한다는 상황을 가정으로 수면을 취하는 동안 변화되는 온도, 습도, 조도를 감지하고, 적정 수면 컨디션을 유지한다. <br>
사용자는 웹을 통해 수면 보조 시스템을 활성화 할 수 있으며, 수면을 취하는 동안 온도, 습도, 조도, 거리 데이터를 수집한다. <br>
수집된 데이터는 웹에서 그래프화 시켜서 보여준다.<br>

## 시스템 구조
<img width="489" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/8fd0e397-d967-47f8-b19d-ae5882947aa4"><br>
<img width="491" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/6d9bcb60-5d1a-493c-9830-e6939b808a3c">

## 하드웨어 구성
하드웨어	라즈베리파이
LED	GPIO6
초음파 센서	Trig = GPIO 20,  Echo = GPIO16
온습도 센서	SCL1, SDA1
조도 센서	MCP3202 사용(SPIMOSI, SPOIMISO, SPISCLK, SPICEO)
스위치	GPIO21
블루투스 스피커	라즈베리파이 내 블루투스
아두이노	USB 단자
DC모터	GPIO5
모터 드라이브		GPIO26

하드웨어	아두이노
릴레이	아두이노 2번 핀
가습기 모듈	릴레이 모듈에 연결

![image](https://github.com/gesal03/HelpSleep/assets/77336664/80872264-5b88-49c8-9bf6-48163470773c)


![image](https://github.com/gesal03/HelpSleep/assets/77336664/666e5be0-4183-4755-80e6-c01f6f61c752)


## 관련 이미지

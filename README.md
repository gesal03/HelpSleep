# HelpSleep
😪 2022 모바일&amp;스마트시스템 Mini Project - 수면 보조 시스템

## 설명
편안한 숙면을 도와주는 시스템이다. 숙면에는 온도, 습도, 조도가 중요하다. <br>
이에 따라 사용자가 수면을 취한다는 상황을 가정으로 수면을 취하는 동안 변화되는 온도, 습도, 조도를 감지하고, 적정 수면 컨디션을 유지한다. <br>
사용자는 웹을 통해 수면 보조 시스템을 활성화 할 수 있으며, 수면을 취하는 동안 온도, 습도, 조도, 거리 데이터를 수집한다. <br>
수집된 데이터는 웹에서 그래프화 시켜서 보여준다.<br>

## 가정 상황
### 상황(1): 침대 모서리에 접근할 경우
침대 한 면에 초음파 센서를 부착한다. 사용자가 수면을 취하며 좌우로 움직이는 상황을 가정하였다. <br>
사용자가 부착된 초음파 센서 과도하게 접근하게 된다면 침대에서 떨어질 위험이 있어 라즈베리파이에 연결된 블루투스 스피커를 통해 경고음을 울린다.<br>
침대 가장자리와의 거리는 웹의 그래프에 지속적으로 출력된다.<br>

### 상황 (2): 수면 적정 습도보다 낮아질 경우
라즈베리파이에 부착된 습도 센서를 통해 방 안의 습도를 측정한다.<br>
숙면에 도움을 주는 적정 습도는 40% ~ 60%이다.<br>
습도 유지를 위해 가습기를 항상 켜놓고, 습도가 적정 습도를 넘어가면 가습기 가동을 종료한다. <br>
위의 가습기는 아두이노와 가습기 모듈을 통해 구현한다. 습도는 웹에 그래프로 지속적으로 출력된다.<br>

### 상황 (3): 수면 적정 조도보다 높아질 경우
방이 어두울수록 숙면에 도움을 준다. 하지만 수면 시 적당한 밝기를 원하는 사용자도 있다. <br>
이러한 사용자를 위하여 라즈베리파이에 부착된LED를 통해 무드등을 구현한다. <br>
본 시스템에서는 조도 센서를 통해 현재 방 안의 조도를 감지하여 무드등을 조절한다.<br> 
조도가 높아지면 LED 밝기를 낮추고, 조도가 낮아지면 LED 밝기를 올리는 방법을 통해 사용자가 원하는 조도 범위에 맞게 방 안의 조도를 조절한다.<br>
조도는 웹에 그래프로 출력된다.<br>

### 상황 (4): 수면 적정 온도보다 높아질 경우
온도가 높으면 수면에 방해가 된다. 실내 온도가 적정 온도를 넘어서게 된다면 선풍기를 가동한다. <br>
온도는 웹에 그래프로 출력된다.<br>


## 시스템 구조
<img width="489" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/8fd0e397-d967-47f8-b19d-ae5882947aa4"><br>
<img width="491" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/6d9bcb60-5d1a-493c-9830-e6939b808a3c">

## 하드웨어 구성
라즈베리 파이와 PC, LED 5개, 초음파 센서 1개, 조도 센서 1개, 스위치 1개, 블루투스 스피커 1개, <br>
DC모터 1개, 모터 드라이브 1개, 아두이노 1개, 릴레이 모듈 1개, 가습기 모듈 1개를 사용한다.<br><br>
![image](https://github.com/gesal03/HelpSleep/assets/77336664/59af8228-06e2-4672-8b54-eaa8aebe303b)
<img width="388" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/ca213cb6-2d0f-4fda-95bf-c697eaf6fe53">

## 관련 이미지

### 초기
1.	웹에서 시작하기 버튼을 눌러 장치들과 연결<br>
2.	장치 동작 여부가 해당 페이지에 출력<br>
3.	센서 값들이 그래프로 출력<br>
<img width="270" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/b731847a-173e-433c-8433-d80f3708bb5b">
<img width="270" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/a22f9687-85e1-4e03-8270-9a31a4475162">

### 침대 가장 자리 접근
침대 가장 자리에 사람(본 이미지에서는 상자로 대체)이 접근하면 블루투스 스피커를 통해 경고음 출력.<br>
<img width="524" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/f40f0cd4-5018-4a4e-a035-13c6f6efdc30">

### 수면 적정 습도보다 높아질 경우
1.	초기 가습기는 가동되고 있다.(좌)<br>
2.	실내 습도가 적정 습도를 넘어서게 된다면 가습기 가동이 중지된다.(우)<br>
<img width="328" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/709809e9-ba9b-4436-9a68-283a6635fbf3">
<img width="332" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/7d130bfa-45e1-4cc0-866d-32078887311f">

### 수면 적정 조도보다 높거나 낮아질 경우
#### 초기
<img width="305" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/35ed07c1-a74f-4abc-83e0-3b2ba7638386">

#### 적정 조도보다 높아졌을 경우
조도가 높아짐에 따라 무드등 밝기가 낮아졌다.<br>
<img width="302" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/0ca555ad-3516-42b2-8d6c-8f76fa584402">

#### 적정 조도보다 낮아졌을 경우
조도가 낮아짐에 따라 무드등 밝기가 높아졌다.<br>
<img width="311" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/51302e13-7d2b-4cfc-a44a-2890826a3eb3">

### 수면 적정 온도보다 높아질 경우
#### 초기
<img width="267" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/ac49b5f4-18cc-4532-b9be-524bdaeb8400">

#### 적정 온도보다 높아질 경우
온도가 높아짐에 따라 선풍기가 가동되었다.<br>
<img width="271" alt="image" src="https://github.com/gesal03/HelpSleep/assets/77336664/df64b640-067d-42cb-990c-4242d9cc7c2e">

## 결론
모바일&스마트 시스템 과목을 수강하며 정말 많은 것을 배웠다.<br>
매번 소프트웨어적으로 동작하는 것만 배워왔다면, 이번 강의를 통해 하드웨어와 결합된 지식을 얻을 수 있어서 의미 있었다.<br>
또한 이번 라즈베리 파이로 프로젝트를 진행하며 하드웨어적 지식을 많이 얻었을 뿐 아니라, <br>
파이썬, JS와 같은 소프트웨어적 지식을 함께 얻을 수 있어서 좋았다.<br>
마지막으로 통신(mqtt 등)과 같은 지식은 모르고 있었는데 이번 강의를 통해서 알게 되어서 의미 있었고, <br>
이번 강의를 통해 얻은 지식을 바탕으로 다양한 모바일 프로젝트를 해보고 싶다.<br>




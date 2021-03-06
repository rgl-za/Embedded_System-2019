# 2019학년도 1학기 임베디드시스템 프로젝트: 오토봇 🚗
## 프로젝트 설명 
차선과 신호등의 상황에 맞게 자율주행하는 RC카

- 개발 환경: Arduino IDE, Thonny Python IDE
- 개발 언어: Python, C언어
- 라이브러리: openCV
- 빌드 도구: CMake

## 프로젝트 목표(개요)
1) 차선과 신호등 인식을 위해 openCV 사용
2) 라즈베리파이와 RC카 연동
3) 라즈베리파이로 데이터 전송을 요청한 RC카가 차선과 신호등의 상황에 맞게 동작
##### e.g. 신호등 상황
+  빨간색: 정지
+  노란색: 서행
+  초록색: (일반) 주행

## 개발과정
#### 1. 라즈베리파이에 파이썬을 통한 openCV 환경 설정
- 리눅스에 라즈베리파이를 연결하여 기본 설정
- python을 업그레이드 하고 추가 라이브러리를 설치
- Cake를 사용하여 python환경에 openCV를 설치
   
#### 2. 영상인식으로 신호등 색 검출
- 라즈베리파이에서 실시간 영상을 불러올 수 있게 함
- 각각의 색의 인식 범위를 정해 정확한 색을 인식할 수 있게 함
- 라즈베리파이에서 얻은 색상값을 간단하게 변환하여 RC카(아두이노)에 전달
- 전달받은 값에 따라 RC카가 다르게 주행할 수 있게 함 

#### 3. 라즈베리파이와 아두이노(RC카)의 시리얼 통신
- 라즈베리파이에서 아두이노 라이브러리를 추가로 설치
- RC카를 연결하여 보드명을 확인한 후 연결 설정
  
    
## 프로젝트 목표 변경 내용
당초 목표: 신호등 변경 인식 ⭕️ , 차선 변경 인식 ⭕️  
⬇️  
목표 변경: 신호등 변경 인식 ⭕️, 차선 변경 인식 ❌

#### 변경 사유: 라즈베리파이 기본 카메라의 해상도가 너무 낮아 변경된 차선을 인식할 때 딜레이가 너무 길어져서 실시간으로 차선을 받아오는 것에 큰 어려움을 겪음, 기본적인 일직선 차선만 인식하여 주행하는 것으로 그쳤음    
    
## 프로젝트 결과물
오토봇 주행 영상: https://youtu.be/Lcezx7SMUgg


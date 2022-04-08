#include <Servo.h>

int MOTORL_PIN = 5;
int MOTORR_PIN = 9;

Servo IServo;
Servo RServo;

int left =1490;
int right =1490;


void setup() {

Serial.begin(115200);

IServo.attach(MOTORL_PIN);
RServo.attach(MOTORR_PIN);
}

void goForward() {

IServo.writeMicroseconds(left+70);
RServo.writeMicroseconds(right-70);

delay(1000);
}

void slow() {

IServo.writeMicroseconds(left+33);
RServo.writeMicroseconds(right-23);

delay(1000);
}

void turnright() {

IServo.writeMicroseconds(left+50);
RServo.writeMicroseconds(right-30);

delay(1000);
}

void turnleft() {

IServo.writeMicroseconds(left+20);
RServo.writeMicroseconds(right-50);

delay(1000);
}

void stop() {

IServo.writeMicroseconds(left);
RServo.writeMicroseconds(right);
}

void back() {

IServo.writeMicroseconds(1400);
RServo.writeMicroseconds(1590);

delay(400);

IServo.writeMicroseconds(1500);
RServo.writeMicroseconds(1490);
}

void loop() {

if (Serial.available()) {

    char value=Serial.read();
    Serial.println(value);

    if(value == 'R'){ // 빨간불
      stop();
      delay(5000);
    }

    if(value == 'Y'){ // 노란불
      slow();
      delay(100);
    }

    if(value == 'G'){ // 초록불
      goForward();
      delay(1000);
    }
  }

  else{
    slow();
  }

}

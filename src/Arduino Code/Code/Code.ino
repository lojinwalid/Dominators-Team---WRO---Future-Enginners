#include <Servo.h>
#define pwm1 11
#define dir1 4
#define dir2 5
int clicked = 0;
Servo myservo;  // create servo object to control a servo
int pushButton = 12;
void setup() {
pinMode(pwm1,OUTPUT);
pinMode(dir1,OUTPUT);
pinMode(dir2,OUTPUT);
myservo.attach(9);
Serial.begin(19200); 
 pinMode(pushButton, INPUT);
}
void loop() {
      int buttonState = digitalRead(pushButton);
       if (buttonState==1){
        clicked=1;
        }
    if(clicked == 1){
   if (Serial.available()) {
    // Read the most recent byte
    String byteRead = Serial.readStringUntil('\n');
    Serial.println(byteRead);
   // ECHO the value that was read
   if(byteRead=="fs"){
    myservo.write(90);
    }
    else if(byteRead=="hr"){
    myservo.write(135);
    }
    else if(byteRead=="mr"){
    myservo.write(115);
    }
    else if(byteRead=="sr"){
    myservo.write(100);
    }
    else if(byteRead=="hl"){
    myservo.write(45);
    }
    else if(byteRead=="ml"){
    myservo.write(65);
    }
    else if(byteRead=="sl"){
    myservo.write(80);
    }
   if(byteRead=="f"){
    forward();
    }
   else if(byteRead=="b"){
    Serial.println("Back");
    backward();
    }
   else if(byteRead=="s"){
    stopyad();
    }
   else if(byteRead=="g"){
    forward_gedan();
    }
   
}
    }
}

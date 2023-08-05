void backward(){
  digitalWrite(dir2,HIGH);
  digitalWrite(dir1,LOW);  
  analogWrite(pwm1,150);
  }
void forward(){
  digitalWrite(dir2,LOW);
  digitalWrite(dir1,HIGH);
  analogWrite(pwm1,185);
  }
  void stopyad(){
  digitalWrite(dir2,LOW);
  digitalWrite(dir1,HIGH);
  analogWrite(pwm1,0);
    
    }
    void forward_gedan(){
  digitalWrite(dir2,LOW);
  digitalWrite(dir1,HIGH);
  analogWrite(pwm1,210); 
  }
    

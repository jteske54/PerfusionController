int speedPin = 11;
//int directionPin = 13;
//int onPin = 12;


void setup() {
  // put your setup code here, to run once:
  pinMode(speedPin, OUTPUT);
  //pinMode(onPin, OUTPUT);
  //pinMode(directionPin, OUTPUT);
  analogWrite(speedPin, 127);
  //digitalWrite(directionPin, LOW);
  //digitalWrite(onPin, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  
}

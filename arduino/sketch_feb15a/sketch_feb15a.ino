int speedPin = 11;
int directionPin = 13;
int onPin = 12;
int recOn;
int recDir;
int recSpeed;
int speedSet;
int directionSet;
int onSet;
int rec;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(19200);
  Serial.setTimeout(100);
  pinMode(speedPin, OUTPUT);
  pinMode(onPin, OUTPUT);
  pinMode(directionPin, OUTPUT);
  digitalWrite(onPin, HIGH);
  analogWrite(speedPin, 127);
  digitalWrite(directionPin, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()){
  rec = Serial.parseInt();
  Serial.println(rec);
  recOn = ((rec % 100)-(rec % 10))/10;
  recDir = (rec % 10);
  recSpeed = floor(rec/100);
  Serial.print(recOn);
  Serial.print(",");
  Serial.print(recDir);
  Serial.print(",");
  Serial.println(recSpeed);
  digitalWrite(onPin, recOn);
  digitalWrite(directionPin, recDir);
  analogWrite(speedPin, recSpeed);
  }
}

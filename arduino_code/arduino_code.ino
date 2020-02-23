#define led 13
#define led2 8
void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  pinMode(8,OUTPUT);
//  digitalWrite(13,LOW);
  digitalWrite(8,LOW);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
//  digitalWrite(13,LOW);
//  digitalWrite(8,LOW);
  if(Serial.read()=='H'){
    digitalWrite(13,HIGH);
    digitalWrite(8,LOW);
    delay(800);
    }
    else if(Serial.read()=='L'){
      digitalWrite(13,LOW);
      digitalWrite(8,HIGH);
      }
}

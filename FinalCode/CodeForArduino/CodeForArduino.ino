const int RELAY_PIN = A5; //Solenoid Lock should be connected to this pin
String incomingByte; //String that we receive from python


void setup() {
  Serial.begin(9600);  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH);
  digitalWrite(LED_BUILTIN, LOW);

}

void loop() {
  if(Serial.available() > 0){
    incomingByte = Serial.readStringUntil('\n');

    if(incomingByte == "2561"){ //THIS NUMBER IS THE PASSWORD
      digitalWrite(RELAY_PIN, LOW);
      delay(3000);
      digitalWrite(RELAY_PIN, HIGH);
    }

      else{
    Serial.write("ERROR");
  }
    
  }

}

String incomingByte ;    

void setup() {

  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);

}
void loop() {

  if (Serial.available() > 0) {

  incomingByte = Serial.readStringUntil('\n');

    if (incomingByte == "on") {

      digitalWrite(LED_BUILTIN, HIGH);

      Serial.write("Led on");

    }

    else if (incomingByte == "off") {

      digitalWrite(LED_BUILTIN, LOW);

      Serial.write("Led off");

    }

    else{

     Serial.write("invald input");

    }

  }

}
//void setup() {
//  // put your setup code here, to run once:
//
//}
//
//void loop() {
//  // put your main code here, to run repeatedly:
//
//}
//
//int x;
//
//void setup() {
//  Serial.begin(115200);
//  Serial.setTimeout(1);
//}
//
//void loop() {
//  while (!Serial.available());
//  x = Serial.readString().toInt();
//  Serial.print(x + 1);
//}

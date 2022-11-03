#include <Key.h>
#include <Keypad.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);

const byte ROWS = 4; 
const byte COLS = 4; 

const int RELAY_PIN = A5; //Solenoid Lock


char password[]= {'3', '2', '4', '2'};
char entered[4];
int pos = 0;

boolean passwordCheck(){
  for (int i = 0;  i < 4; i++){
    if( entered[i] != password[i] ){
      return false;
    }
  }
  return true;
}

int number = 0;

void setup(){
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();

  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN,HIGH);

  Serial.println("Enter Password");
  
}
  
void loop(){
  number = 0;

  while(Serial.available() == 0){ /*do nothing*/}

  while(Serial.available()){
    int incoming = Serial.read();
    Serial.println(incoming);

    if(incoming == 49){
      delay(1000);
      digitalWrite(RELAY_PIN, LOW);  // Bounce out
      delay(2000);
      digitalWrite(RELAY_PIN, HIGH); // Lock in
    }
  }
}
  
//  char customKey = customKeypad.getKey();
//  
//  if (customKey){
//    lcd.print(customKey);
//    entered[pos] = customKey;
//    pos++;
//  }
//
//  if (pos==4){
//    if( passwordCheck()){
//      lcd.clear();
//      lcd.print("BRAVO");
//      digitalWrite(RELAY_PIN, LOW);  // Bounce out
//      delay(2000);
//      digitalWrite(RELAY_PIN, HIGH); // Lock in
//    }
//    else{
//      lcd.clear();
//      lcd.print("ERREUR");
//      delay(3000);  
//    }
//    lcd.clear();
//    entered[4]={}; 
//  }
//}

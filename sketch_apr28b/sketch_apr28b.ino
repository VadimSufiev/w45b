#include <PRIZM.h>    
PRIZM prizm;          

int incomingByte = 0;

void setup() {
  Serial.begin(9600);
  prizm.PrizmBegin();  
}

void loop() {

  if (Serial.available() > 0)
  {
    incomingByte = Serial.read();

    if (incomingByte == 49)
    {
      prizm.setMotorPower(1, 25);                
      prizm.setMotorPower(2, -25);
    }

    if (incomingByte == 50)
    {
      prizm.setMotorPower(1, 0);                
      prizm.setMotorPower(2, 0);
    }

    Serial.println(incomingByte, DEC);
  }
}

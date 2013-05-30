/*
Lights
This reads 3 bytes of info from the serial port and sets the PWM of 3 pins
based on that value. 

All code is licensed under the GNU GPL, Version 2 or later. 

 */


//The pins that the colors are connected to. 
int redLed = 9; 
int greenLed = 11;
int blueLed = 10;

// The default color of the lights. 
int redValue = 255; 
int greenValue = 160; 
int blueValue = 60; 


//set the color of the lights. 
void setColor(int red, int green, int blue)
{ 
  analogWrite(redLed, red); 
  analogWrite(greenLed, green); 
  analogWrite(blueLed, blue); 
} 

// the setup routine runs once when you press reset:
void setup()  { 
  //start the serial port.
  Serial.begin(9600); 
  
  pinMode(redLed, OUTPUT); 
  pinMode(greenLed, OUTPUT);
  pinMode(blueLed, OUTPUT); 

  setColor(redValue, greenValue, blueValue); 
} 

// the loop routine runs over and over again forever:
void loop()  { 
  if (Serial.available()) {
    //read 3 bytes. 
    redValue = Serial.read();
    greenValue = Serial.read(); 
    blueValue = Serial.read(); 
    // set the color. 
    setColor(redValue, greenValue, blueValue); 
  }
}

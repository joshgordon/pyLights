/*
Lights
This reads 3 bytes of info from the serial port and sets the PWM of 3 pins
based on that value. 

All code is licensed under the GNU GPL, Version 2 or later. 

 */


//The pins that the colors are connected to. 
int redLedA = 9; 
int greenLedA = 11;
int blueLedA = 10;

int redLedB = 5; 
int greenLedB = 3;
int blueLedB = 6;


// The default color of the lights. 
int redValueA = 15; 
int greenValueA = 0; 
int blueValueA = 0; 

// The default color of the lights. 
int redValueB = 15; 
int greenValueB = 0; 
int blueValueB = 0; 


//set the color of the lights. 
void setColorA(int red, int green, int blue)
{ 
  analogWrite(redLedA, red); 
  analogWrite(greenLedA, green); 
  analogWrite(blueLedA, blue); 

} 

//set the color of the lights. 
void setColorB(int red, int green, int blue)
{ 
  
  analogWrite(redLedB, 255 - red); 
  analogWrite(greenLedB, 255 - green); 
  analogWrite(blueLedB, 255 - blue); 

} 

// the setup routine runs once when you press reset:
void setup()  { 
  //start the serial port.
  Serial.begin(9600); 
  
  pinMode(redLedA, OUTPUT); 
  pinMode(greenLedA, OUTPUT);
  pinMode(blueLedA, OUTPUT); 


  pinMode(redLedB, OUTPUT); 
  pinMode(greenLedB, OUTPUT);
  pinMode(blueLedB, OUTPUT); 

  setColorA(redValueA, greenValueA, blueValueA); 
  setColorB(redValueB, greenValueB, blueValueB); 
} 

// the loop routine runs over and over again forever:
void loop()  { 
  if (Serial.available()) {
    char control = Serial.read(); 
    
    //Check to see if we're controlling strip A
    if (control == 'a')
      { 
	//read 3 bytes. 
	redValueA = Serial.read();
	greenValueA = Serial.read(); 
	blueValueA = Serial.read(); 
	// set the color. 
	setColorA(redValueA, greenValueA, blueValueA); 
      } 
    else if (control == 'A')
      { 
	Serial.print("["); 
	Serial.print(redValueA); 
	Serial.print(", "); 
	Serial.print(greenValueA); 
	Serial.print(", "); 
	Serial.print(blueValueA); 
	Serial.print("]"); 
      }
    else if (control == 'b')
      { 
	//read 3 bytes. 
	redValueB = Serial.read();
	greenValueB = Serial.read(); 
	blueValueB = Serial.read(); 
	// set the color. 
	setColorB(redValueB, greenValueB, blueValueB); 
      } 
    else if (control == 'B')
      { 
	Serial.print("["); 
	Serial.print(redValueB); 
	Serial.print(", "); 
	Serial.print(greenValueB); 
	Serial.print(", "); 
	Serial.print(blueValueB); 
	Serial.print("]"); 
      }
  }

}
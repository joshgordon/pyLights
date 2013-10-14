#Defines a single RGB color. Also includes function for setting color based on
# arbitrary RGB values. 
# Written by Josh Gordon (github.com/joshgordon) 
# All code is licensed under the GNU GPL, Version 2 or later. 

import fade

# Sorry for the lack of comments, I kinda threw this together quickly... 

class Color: 
    """A single color"""

    red = 0
    green = 0
    blue = 0

    def __init__(self, ser, red, green, blue): 
        self.red = red
        self.green = green
        self.blue = blue
        self.ser = ser

    def setA(self): 
        self.ser.write('a' + chr(self.red) + chr(self.green) + chr(self.blue))

    def setB(self): 
        self.ser.write('b' + chr(self.red) + chr(self.green) + chr(self.blue))
        
    def fadeA(self, current, time): 
        fade.fade(self.ser, time, "a", current, (self.red, self.green, self.blue))

    def fadeB(self, current, time): 
        fade.fade(self.ser, time, "b", current, (self.red, self.green, self.blue))

def setA(ser, r, g, b): 
    ser.write('a' + chr(r) + chr(g) + chr(b))


def setB(ser, r, g, b): 
    ser.write('b' + chr(r) + chr(g) + chr(b))

def setW(ser, b): 
    ser.write('w' + chr(b))

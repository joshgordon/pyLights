#Defines a single RGB color. Also includes function for setting color based on
# arbitrary RGB values. 
# Written by Josh Gordon (github.com/joshgordon) 
# All code is licensed under the GNU GPL, Version 2 or later. 


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

    def set(self): 
        self.ser.write(chr(self.red) + chr(self.green) + chr(self.blue))

def set(ser, r, g, b): 
    ser.write(chr(r) + chr(g) + chr(b))

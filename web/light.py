# Uses the color class and a dictionary to have a set of colors. More will be 
# here soon. 
# Written by Josh Gordon (github.com/joshgordon) 
# All code is licensed under the GNU GPL, Version 2 or later. 


# Sorry for the lack of comments, I kinda threw this together quickly... 

import serial
import color
from time import sleep
from __future__ import print_function
import sys
import time 

#set up the serial port. 
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

class ColorLight: 
    def __init__(lightSet): 
        valid=['a', 'b'] # Valid Light sets. 
        self.ser = ser
        self.colors=3
        if lightSet in valid: 
            color = getColorTuple(lightSet)
            self.r = color[0]
            self.g = color[1] 
            self.b = color[2] 
            self.lightSet = lightSet
        else: 
            raise Exception("Invalid Light") 
        
    def setColor(self, color): 
        print("Setting color {0} {1} {2}".format(color[0], color[1], color[2]), file=sys.stderr) 
        self.r = color[0] 
        self.g = color[1]
        self.b = color[2] 
        self.ser.write(self.lightSet + chr(self.r) + chr(self.g) + chr(self.b))
        

    ## The main point of this is to keep overhead down when fading. 
    def setDirect(self, color): 
        self.ser.write(self.lightSet + chr(color[0]) + chr(color[1]) + chr(color[2]))
        
    def setColorByName(self, colorName): 
        r, g, b = color.getColor(colorName)
        self.setColor(r, g, b)
        


    def fade(self, fTime, end): 
        exp= 4/3.0
        start=self.getColor() 
        for i in range(65): 
            current = list() 
            for c in range(self.colors): 
                if end[c] > start[c]: 
                    current.append(int((end[c]-start[c])/256.0 * i ** exp + start[c]))
                else: 
                    current.append(int(start[c] - (start[c]-end[c])/255.0 * i ** exp))
                    
            self.setDirect(current[0], current[1], current[2])
            time.sleep(fTime/64.0)

        # make sure we update the variables. 
        self.setColor(r, g, b)

    def fadeByName(self, fTime, colorName): 
        thisColor = color.getColor(colorName) 
        self.fade(fTime, thisColor) 
                
            
    def getColor(self): 
        return (self.r, self.g, self.b) 


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

#set up the serial port. 
ser = serial.Serial('/dev/tty.usbmodemfd1221', 9600, timeout=1)

class ColorLight: 
    def __init__(lightSet): 
        valid=['a', 'b'] # Valid Light sets. 
        self.ser = ser
        if lightSet in valid: 
            color = getColorTuple(lightSet)
            self.r = color[0]
            self.g = color[1] 
            self.b = color[2] 
            self.lightSet = lightSet
        else: 
            raise Exception("Invalid Light") 
        
    def setColor(self, r, g, b): 
        print("Setting color {0} {1} {2}".format(r, g, b), file=sys.stderr) 
        self.r = r
        self.g = g
        self.b = b 
        self.ser.write(self.lightSet + chr(self.r) + chr(self.g) + chr(self.b))
        

    def setColorByName(self, colorName): 
        colors[colorName].getColor()
        



def getColor(set): 
    ser.write(set.upper()) 
    ##This is ugly, but I really don't feel like reflashing the arduino
    # to turn it into something prettier... 
    return list(str(ser.readline()).strip().split(','))
    # return allCols
    # return list([75, 83, 23] )
        
def getColorTuple(set): 
    color = getColor(set)
    return map(int, color)
    
colors = dict()

colors['red'] = color.Color(ser, 255, 0, 0) 
colors['green'] = color.Color(ser, 0, 255, 0)
colors['blue'] = color.Color(ser, 0, 0, 255)
colors['white'] = color.Color(ser, 255, 160, 60) 
colors['black'] = color.Color(ser, 0, 0, 0)
colors['11pm'] = color.Color(ser, 75, 25, 1)
colors['midnight'] = color.Color(ser, 50, 10, 0)
colors['1am'] = color.Color(ser, 25, 5, 0)
colors['dimWhite'] = color.Color(ser, 50, 10, 3)

def setA(r, g, b)

#print "setting red" 
# colors['red'].set(ser)
# sleep(5)
# print "setting white" 
# colors['white'].set(ser)

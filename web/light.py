# Uses the color class and a dictionary to have a set of colors. More will be
# here soon.
# Written by Josh Gordon (github.com/joshgordon)
# All code is licensed under the GNU GPL, Version 2 or later.


# Sorry for the lack of comments, I kinda threw this together quickly...

from __future__ import print_function
import serial
# import colors
from time import sleep
import sys
import time
import threading

#set up the serial port.
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)



class ColorLight:
    def __init__(self, lightSet):
        valid=['a', 'b'] # Valid Light sets.
        self.ser = ser
        self.colors=3
        if lightSet in valid:
            # color = getColorTuple(lightSet)
            self.r = 0
            self.g = 0
            self.b = 0
            self.lightSet = bytes(lightSet, 'ascii')

        else:
            raise Exception("Invalid Light")

    def setColor(self, color):
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.ser.write(self.lightSet + bytes([self.r]) + bytes([self.g]) + bytes([self.b]))


    ## The main point of this is to keep overhead down when fading. 
    def setDirect(self, color):
        self.ser.write(self.lightSet + bytes([color[0]]) + bytes([color[1]]) + bytes([color[2]]))

#    def setColorByName(self, colorName):
#        r, g, b = color.getColor(colorName)
#        self.setColor(r, g, b)

    def fade(self, fTime, end):
        start = self.getColor()
        self.r = end[0]
        self.g = end[1]
        self.b = end[2]
        threading.Thread(target=self.fadeReal, args=(fTime, start, end)).start()

    def fadeReal(self, fTime, start, end):
        exp= 4/3.0
        for i in range(65):
            current = list()
            for c in range(self.colors):
                if end[c] > start[c]:
                    current.append(int((end[c]-start[c])/256.0 * i ** exp + start[c]))
                else:
                    current.append(int(start[c] - (start[c]-end[c])/255.0 * i ** exp))

            self.setDirect((current[0], current[1], current[2]))
            time.sleep(fTime/64.0)

        # make sure we update the variables.
        self.setColor(end)


#TODO
#    def fadeByName(self, fTime, colorName):
#        thisColor = color.getColor(colorName)
#        self.fade(fTime, thisColor)


    def getColor(self):
        return (self.r, self.g, self.b)


class MonoLight:
    def __init__(self, lightSet):
        valid=['w'] # valid Light sets.
        self.ser = ser
        self.colors=1
        if lightSet in valid:
            #color=getColorTuple(lightSet)
            self.b = 0
            self.lightSet = bytes(lightSet, 'ascii')
        else:
            raise Exception("Invalid Light")


    def setColor(self, color):
        self.b = color[0]
        self.ser.write(self.lightSet + bytes([self.b]))


    def setDirect(self, color):
        self.ser.write(self.lightSet + bytes([color[0]]))

    def fade(self, fTime, end):
        start = self.getColor()[0]
        self.b = end[0]
        threading.Thread(target=self.fadeReal, args=(fTime, start, end)).start()

    def fadeReal(self, fTime, start, end):
        exp=4/3.0
        end = end[0]
        for i in range(65):
            if end > start:
                current=(int((end-start)/256.0 * i ** exp + start))
            else:
                current=(int(start - (start-end)/255.0 * i ** exp))

            self.setDirect((current, ))
            time.sleep(fTime/64.0)

        self.setColor((end, ))


    def getColor(self):
        return (self.b, )


# def getColor(set):
#     ser.write(set.upper())
#     ##This is ugly, but I really don't feel like reflashing the arduino
#     # to turn it into something prettier...
#     return list(str(ser.readline()).strip().split(','))
#     # return allCols
#     # return list([75, 83, 23] )

# def getColorTuple(set):
#     color = getColor(set)
#     return map(int, color)

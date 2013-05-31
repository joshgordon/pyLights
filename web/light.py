# Uses the color class and a dictionary to have a set of colors. More will be 
# here soon. 
# Written by Josh Gordon (github.com/joshgordon) 
# All code is licensed under the GNU GPL, Version 2 or later. 


# Sorry for the lack of comments, I kinda threw this together quickly... 

import serial
import color
from time import sleep

#set up the serial port. 
ser = serial.Serial('/dev/serial/by-id/usb-Arduino_LLC_Arduino_Leonardo-if00', 9600, timeout=1)


colors = dict()

colors['red'] = color.Color(ser, 255, 0, 0) 
colors['green'] = color.Color(ser, 0, 255, 0)
colors['blue'] = color.Color(ser, 0, 0, 255)
colors['white'] = color.Color(ser, 255, 160, 60) 
colors['black'] = color.Color(ser, 0, 0, 0)
colors['11pm'] = color.Color(ser, 75, 20, 3)
colors['midnight'] = color.Color(ser, 50, 10, 0)
colors['1am'] = color.Color(ser, 25, 5, 0)

#print "setting red" 
# colors['red'].set(ser)
# sleep(5)
# print "setting white" 
# colors['white'].set(ser)

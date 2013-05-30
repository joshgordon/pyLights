# Uses the color class and a dictionary to have a set of colors. More will be 
# here soon. 
# Written by Josh Gordon (github.com/joshgordon) 
# All code is licensed under the GNU GPL, Version 2 or later. 


# Sorry for the lack of comments, I kinda threw this together quickly... 

import serial
import color
from time import sleep

#set up the serial port. 
ser = serial.Serial('/dev/tty.usbmodemfa131', 9600, timeout=1)


colors = dict()

colors['red'] = color.Color(255, 0, 0) 
colors['green'] = color.Color(0, 255, 0) 
colors['blue'] = color.Color(0, 0, 255) 
colors['white'] = color.Color(255, 160, 60) 

#print "setting red" 
# colors['red'].set(ser)
# sleep(5)
print "setting white" 
colors['white'].set(ser)

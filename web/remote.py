#!/usr/bin/env python

import light 
import RPi.GPIO as GPIO 
import http.client
import os
from xmlrpc.client import ServerProxy, Error
from time import sleep

desk = light.ColorLight('a')  
window = light.ColorLight('b')  
work = light.MonoLight('w')   

relays = ServerProxy("http://192.168.1.19:8000")

fadeTime = 0.7

buttons = [17, 18, 24, 22, 23, 4] # These are in order, in natural
                                  # order when you hold the darned
                                  # thing upright.

vars = ['desk', 'window', 'work', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 
        'r7', 'r8', 'mac']

presets = [
  # All on
  {
    'desk': (255, 55, 15), 'window': (255, 55, 15), 'work': (255, ),
    'r1': True, 'r2': True, 'r3': True, 'r4': True, 'r6': True, 'mac': True
  }, 

  # Red
  {'desk': (255, 0, 0), 'window': (255, 0, 0), 'work': (15,)}, 
  
  # Blue
  {'desk': (0, 0, 255), 'window': (0, 0, 255), 'work': (0,), 'r4': False}, 

  # Green
  {'desk': (255, 0, 0), 'window': (0, 255, 0), 'work': (0,)},

  # Lights off
  {'desk': (0, 0, 0), 'window': (0, 0, 0), 'work': (0,), 'r4': False}, 
  
  # All Off. 
  {
    'desk': (0, 0, 0), 'window': (0, 0, 0), 'work': (0, ),
    'r1': False, 'r2': False, 'r3': False, 'r4': False, 'r6': True, 
    'mac': False
  }, 

]

def setPreset(number): 
  preset = presets[number]
  
  for var in vars: 
    if var in preset: 
      if var == 'desk': 
        desk.fade(fadeTime, preset['desk'])
      elif var == 'window': 
        window.fade(fadeTime, preset['window'])
      elif var == 'work': 
        work.fade(fadeTime, preset['work'])
      elif var == 'mac': 
        mac(preset['mac'])
        
      elif var[0] == 'r': 
        if preset[var]: 
          relays.on(int(var[1]))
        else: 
          relays.off(int(var[1]))
        
  

def mac(state): 
  if state: 
    print("Mac on")
    os.system("ssh josh@ferengi caffeinate -u true") 
  else: 
    print("Mac off")
    os.system("ssh josh@ferengi pmset displaysleepnow")

mostRecentButton = -1
working = False
def buttonHandler(button): 
  global working
  if working == True: 
    return
  else:
    working = True
    global mostRecentButton
    for i in range(len(buttons)): 
      if GPIO.input(buttons[i]) == 1: 
        if mostRecentButton != i:
          setPreset(i)
          mostRecentButton = i
        break
    sleep(.01)
    working = False


GPIO.setmode(GPIO.BCM)

for button in buttons: 
  GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  #Second switch
  GPIO.add_event_detect(button,  GPIO.BOTH, callback=buttonHandler, bouncetime=200)


while True: 
  sleep(100)

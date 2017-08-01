#!/usr/bin/env python

#import light 
import RPi.GPIO as GPIO 
import http.client
import os
from xmlrpc.client import ServerProxy, Error
from time import sleep
from bottle import route, request, run, get, redirect, static_file 

#desk = light.ColorLight('a')  
#window = light.ColorLight('b')  
#work = light.MonoLight('w')   

relays = ServerProxy("http://pyrelay:8000")

fadeTime = 0.7

buttons = [17, 18, 24, 22, 23, 4] # These are in order, in natural
                                  # order when you hold the darned
                                  # thing upright.

vars = ['r7', 'r8', 'r4', 'r5', 'r6', 'r1', 'r2', 'r3', 
        'mac'] # 'desk', 'window', 'work', 

presets = [
  # All on
  {
    'r1': True, 'r2': True, 'r3': True, 'r4': True, 'r5': True, 'r6': True,
    'r7': True, 'r8': True, 'mac': True
  }, 

  # Red
  { 'r5': True, 'r6': True}, 
  
  # Blue
  {'r5': False}, 

  # Green
  {'r6': False},

  # Lights off
  {'r5': False, 'r6': False, 'r7': True, 'r8': True, 'mac': True}, 
  
  # All Off. 
  {
    'r2': False, 'r3': False, 'r4': False, 'r5': False, 'r6': False, 'r7': False, 'r8': False, 
    'mac': False
  }, 

]

def setPreset(number): 
  preset = presets[number]
  
  for var in vars: 
    print("...")
    if var in preset: 
#      if var == 'desk': 
#        desk.fade(fadeTime, preset['desk'])
#      elif var == 'window': 
#        window.fade(fadeTime, preset['window'])
#      elif var == 'work': 
#        work.fade(fadeTime, preset['work'])
      if var == 'mac': 
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

@route("/push/<button>")
def webHandler(button):
  mostRecentbutton = int(button)
  setPreset(int(button))

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
          print("Button pressed %d." % i) 
          mostRecentButton = i
        break
    sleep(.01)
    working = False
    print("No longer working.")


GPIO.setmode(GPIO.BCM)

for button in buttons: 
  GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  #Second switch
  GPIO.add_event_detect(button,  GPIO.BOTH, callback=buttonHandler, bouncetime=200)

@route('/')
def default():
  return static_file('buttons.html', root='/root/pyLights/web')


run(host="0.0.0.0", port=8080)
# while True: 
  
#   sleep(1000000)

#!/usr/bin/env python2 
from bottle import route, request, run, get, template

import light 

a = light.ColorLight('a') 
b = light.ColorLight('b') 
w = light.MonoLight('w') 


@route('/on')
def on(): 
  w.fade(.3, 255)
  b.fade(.3, (255, 25, 0))
  a.fade(.3, (255, 25, 0))

@route('/off')
def off(): 
  a.fade(.3, (0, 0, 0))
  b.fade(.3, (0, 0, 0))
  w.fade(.3, 0) 
  
@route('/desk/<red>/<green>/<blue>')
@route('/a/<red>/<green>/<blue>')
def setA(red, green, blue): 
  a.setColor((int(red), int(green), int(blue)))

@route('/window/<red>/<green>/<blue>')
@route('/b/<red>/<green>/<blue>')
def setB(red, green, blue): 
  b.setColor((int(red), int(green), int(blue)))

@route('/work/<bright>') 
@route('/w/<bright>')
def setW(bright): 
  w.setBrightness(int(bright))


################################################################################
@route('/fade/<fTime>/desk/<red>/<green>/<blue>')
@route('/fade/<fTime>/a/<red>/<green>/<blue>')
def fadeA(fTime, red, green, blue): 
  a.fade(float(fTime), (int(red), int(green), int(blue)))

@route('/fade/<fTime>/window/<red>/<green>/<blue>')
@route('/fade/<fTime>/b/<red>/<green>/<blue>')
def fadeB(fTime, red, green, blue): 
  b.fade(float(fTime), (int(red), int(green), int(blue)))

@route('/fade/<fTime>/work/<bright>') 
@route('/fade/<fTime>/w/<bright>')
def fadeW(fTime, bright): 
  w.fade(float(fTime), int(bright))

################################################################################

defaultFade=0.7

@route('/fade/desk/<red>/<green>/<blue>')
@route('/fade/a/<red>/<green>/<blue>')
def fadeDefaultA(red, green, blue): 
  a.fade(defaultFade, (int(red), int(green), int(blue)))

@route('/fade/window/<red>/<green>/<blue>')
@route('/fade/b/<red>/<green>/<blue>')
def fadeDefaultB(red, green, blue): 
  b.fade(defaultFade, (int(red), int(green), int(blue)))

@route('/fade/work/<bright>') 
@route('/fade/w/<bright>')
def fadeDefaultW(bright): 
  w.fade(defaultFade, int(bright))






run(host='0.0.0.0', port=80)


#!/usr/bin/env python2 
from bottle import route, request, run, get, template, redirect, static_file

import light, json, os 

a = light.ColorLight('a') 
b = light.ColorLight('b') 
w = light.MonoLight('w') 

lights = [a, b, w]

@route('/on')
def on(): 
  w.fade(.3, (255, ))
  b.fade(.3, (255, 55, 25))
  a.fade(.3, (255, 55, 25))
  return redirect('/', code=302)

@route('/off')
def off(): 
  a.fade(.3, (0, 0, 0))
  b.fade(.3, (0, 0, 0))
  w.fade(.3, (0, )) 
  return redirect('/', code=302)
  
@route('/desk/<red>/<green>/<blue>')
@route('/a/<red>/<green>/<blue>')
def setA(red, green, blue): 
  a.setColor((int(red), int(green), int(blue)))
  return redirect('/', code=302)

@route('/window/<red>/<green>/<blue>')
@route('/b/<red>/<green>/<blue>')
def setB(red, green, blue): 
  b.setColor((int(red), int(green), int(blue)))
  return redirect('/', code=302)

@route('/ab/<red>/<green>/<blue>')
def setBoth(red, green, blue): 
  a.setColor((int(red), int(green), int(blue)))
  b.setColor((int(red), int(green), int(blue)))
  return redirect('/', code=302)
  

@route('/work/<bright>') 
@route('/w/<bright>')
def setW(bright): 
  w.setBrightness((int(bright), ))
  return redirect('/', code=302)


################################################################################
@route('/fade/<fTime>/desk/<red>/<green>/<blue>')
@route('/fade/<fTime>/a/<red>/<green>/<blue>')
def fadeA(fTime, red, green, blue): 
  a.fade(float(fTime), (int(red), int(green), int(blue)))
  return redirect('/', code=302)

@route('/fade/<fTime>/window/<red>/<green>/<blue>')
@route('/fade/<fTime>/b/<red>/<green>/<blue>')
def fadeB(fTime, red, green, blue): 
  b.fade(float(fTime), (int(red), int(green), int(blue)))
  return redirect('/', code=302)

@route('/fade/<fTime>/work/<bright>') 
@route('/fade/<fTime>/w/<bright>')
def fadeW(fTime, bright): 
  w.fade(float(fTime), (int(bright), ))
  return redirect('/', code=302)

################################################################################

defaultFade=0.7

@route('/fade/desk/<red>/<green>/<blue>')
@route('/fade/a/<red>/<green>/<blue>')
def fadeDefaultA(red, green, blue): 
  a.fade(defaultFade, (int(red), int(green), int(blue)))
  return redirect('/', code=302)

@route('/fade/window/<red>/<green>/<blue>')
@route('/fade/b/<red>/<green>/<blue>')
def fadeDefaultB(red, green, blue): 
  b.fade(defaultFade, (int(red), int(green), int(blue)))
  return redirect('/', code=302)


@route('/fade/work/<bright>') 
@route('/fade/w/<bright>')
def fadeDefaultW(bright): 
  w.fade(defaultFade, (int(bright), ))
  return redirect('/', code=302)

@route('/post', method='POST') 
def handle_post(): 
  a_red = request.forms.get('a_red') 
  a_grn = request.forms.get('a_grn') 
  a_blu = request.forms.get('a_blu') 
  a_fad = request.forms.get('a_fad') 

  b_red = request.forms.get('b_red') 
  b_grn = request.forms.get('b_grn') 
  b_blu = request.forms.get('b_blu') 
  b_fad = request.forms.get('b_fad') 
  
  w_brt = request.forms.get('w_brt')
  w_fad = request.forms.get('w_fad')
  
  
  if a_red != None: 
    try: 
      a.fade(float(a_fad), (int(a_red), int(a_grn), int(a_blu)))
    except: 
      a.setColor((int(a_red), int(a_grn), int(a_blu)))

  if b_red != None: 
    try: 
      b.fade(float(b_fad), (int(b_red), int(b_grn), int(b_blu)))
    except: 
      b.setColor((int(b_red), int(b_grn), int(b_blu)))

  if w_brt != None: 
    try: 
      w.fade(float(w_fad), (int(w_brt), ))
    except: 
      w.setColor((int(w_brt), ))
      
  return redirect("/", code=302)

@route('/toggle') 
def toggleState(): 
  a_color = a.getColor() 
  b_color = b.getColor() 
  w_color = w.getColor() 
  sum = 0
  for color in a_color: 
   sum += color
  for color in b_color: 
   sum += color
  for color in w_color: 
   sum += color

  if sum > 0: 
    off() 
  else: 
    on() 

@route('/') 
def homePage(): 
  cwd = os.path.dirname(os.path.realpath(__file__))
  return static_file('index.html', root=cwd)

@route('/colors')
def colors(): 
  return json.dumps({"a": a.getColor(), "b": b.getColor(), "w": w.getColor()})


@route('/favicon.ico') 
def favicon(): 
  cwd = os.path.dirname(os.path.realpath(__file__))
  return static_file('./favicon.ico', root=cwd)

@route('/jquery.js')
def jquery(): 
  cwd = os.path.dirname(os.path.realpath(__file__))
  return static_file('./jquery-2.1.1.min.js', cwd)

@route('/jquery-ui.js')
def jqueryUI(): 
  cwd = os.path.dirname(os.path.realpath(__file__))
  return static_file('./jquery-ui.js', cwd) 

run(host='0.0.0.0', port=8088)


#!/usr/bin/env python2 
from bottle import route, request, run, get, template, redirect

import light 

a = light.ColorLight('a') 
b = light.ColorLight('b') 
w = light.MonoLight('w') 

lights = [a, b, w]

@route('/on')
def on(): 
  w.fade(.3, (255, ))
  b.fade(.3, (255, 25, 0))
  a.fade(.3, (255, 25, 0))
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


@route('/') 
def homePage(): 
  a_color = a.getColor() 
  b_color = b.getColor() 
  w_color = w.getColor() 
  return template("""

  <html> 
  <head>
  <meta charset="utf-8">
  <title>Desk Light Control</title>


  </head> 

  <a href="/on">On</a> <a href="/off">off</a> 

  <h1>Light Control</h1> 
  <body>
  <form action="/post" method="post"> 
  <table>
  <tr> 
  <td> 
  <h2> Desk light </h2> 
  <table>
  <tr> <td> <label for="a_red">Red</label></td><td><input type="text" name="a_red" value="{{a_red}}"/> </td> </tr> 
  <tr> <td> <label for="a_grn">Green</label></td> <td> <input type="text" name="a_grn" value="{{a_grn}}"/>  </td> </tr> 
  <tr> <td> <label for="a_blu">Blue</label></td> <td> <input type="text" name="a_blu" value="{{a_blu}}"/> </td> </tr> 
  <tr> <td> <label for="a_fad">Fade Time</label></td> <td> <input type="text" name="a_fad" />  </td> </tr> 
  </table> 

  </td> 
  
  <td>
  <h2> Window Light </h2> 
  <table>
  <tr> <td> <label for="b_red">Red</label></td><td><input type="text" name="b_red" value="{{b_red}}"/> </td> </tr> 
  <tr> <td> <label for="b_grn">Green</label></td> <td> <input type="text" name="b_grn" value="{{b_grn}}"/>  </td> </tr> 
  <tr> <td> <label for="b_blu">Blue</label></td> <td> <input type="text" name="b_blu" value="{{b_blu}}"/> </td> </tr> 
  <tr> <td> <label for="b_fad">Fade Time</label></td> <td> <input type="text" name="b_fad" />  </td> </tr> 
  </table> 

  </td> 
  
  <td> 
  <h2> Work Light </h2> 
  <table>
  <tr> <td> <label for="w_brt">Brightness</label></td> <td> <input type="text" name="w_brt" value="{{w_brt}}"/> </td> </tr> 
  <tr> <td> <label for="w_fad">Fade Time</label></td> <td> <input type="text" name="w_fad" />  </td> </tr> 
  </table> 
  </td> 
  </tr> 
  </table> 
  <input type="submit" /> 
  </form> 
  </body> 
  </html> 
  """, 
                  a_red=a_color[0], a_grn=a_color[1], a_blu = a_color[2], 
                  b_red=b_color[0], b_grn=b_color[1], b_blu = b_color[2], 
                  w_brt=w_color[0]) 




run(host='0.0.0.0', port=80)


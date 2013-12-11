import light
import color

print '<html><head><link href="favicon.ico" rel="icon" type="image/x-icon" />' 
print '</head><body>'
print "<h1>RGB Light Control</h1>"

if request: 
    if 'redA' in request: 
        redA=int(request['redA'][0])
        greenA=int(request['greenA'][0])
        blueA=int(request['blueA'][0])
        color.setA(light.ser, redA, greenA, blueA)
    if 'redB' in request:
        redB=int(request['redB'][0])
        greenB=int(request['greenB'][0])
        blueB=int(request['blueB'][0])
        color.setB(light.ser, redB, greenB, blueB)

            
    if 'colorA' in request: 
        color=request['colorA'][0]
        light.colors[color].setA() 
    if 'colorB' in request: 
        color=request['colorB'][0]
        light.colors[color].setB()
    if 'color' in request: 
        color=request['color'][0]
        light.colors[color].setA()
        light.colors[color].setB()

    if 'white' in request: 
        color.setW(light.ser, int(request['white'][0]))
    
    elif 'off' in request: 
        color.setA(light.ser, 0, 0, 0)
        color.setB(light.ser, 0, 0, 0)
        color.setW(light.ser, 0) 


print '<h1><a href="index.py?off">All Lights off</a></h1>' 

print '<h2>Enter your own RGB color or pick from the list. </h2>'
print '<table><tr>' 

print '<form action="index.py" method="post">'

for set in ['a', 'b', 'w']: 
    
    colors = light.getColor(set) 

    if set in ('a', 'b'):
        red = colors[0]
        green = colors[1]
        blue = colors[2]
    else: 
        white = colors[0]

    if set == 'a': 
        print '<td><h3>Desk Light</h3>'
    elif set == 'b': 
        print '<td><h3>Window Light</h3>'
    elif set == 'w': 
        print '<td><h3>Work Light</h3>' 

    print '<table>' 

    if set == 'a': 
        print '<tr><td>Red: </td><td><input type="text" name="redA" value=', red, '></td></tr>'
        print '<tr><td>Green: </td><td><input type="text" name="greenA" value=', green, '></td></tr>' 
        print '<tr><td>Blue: </td><td><input type="text" name="blueA" value=', blue, '></td></tr>' 


    elif set == 'b':  
        print '<tr><td>Red: </td><td><input type="text" name="redB" value=', red, '></td></tr>'
        print '<tr><td>Green: </td><td><input type="text" name="greenB" value=', green, '></td></tr>' 
        print '<tr><td>Blue: </td><td><input type="text" name="blueB" value=', blue, '></td></tr>' 

    else: 
        print '<tr><td>Brightness: </td><td><input type="text" name="white" value=', white, '></td></tr>'

    print '</table>'
    
    # if set in ('a', 'b'): 
    #     print '<form action="index.py" method="post">' 
    #     print '<input type="hidden" name="light" value="' + set + '">' 
    #     print '<select name=color>' 
    #     for col in light.colors: 
    #         print '<option value="' + col + '">' + col.title() + '</option>'
    #     print '</select> <input type="submit" value="set"></form>' 

    print '</td>' 

print '<input type="submit" value="set">'
    
print '</form></tr></table>'

# print '<form action="index.py" method="post"><input type="hidden" name="off" value="">' 
# print '<input type="submit" value="All off"> </form> ' 

print '</body></html>'

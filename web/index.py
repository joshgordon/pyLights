import light
import color

print "<h1>RGB Light Control</h1>"

if request: 
    if 'red' in request: 
        red=int(request['red'][0])
        green=int(request['green'][0])
        blue=int(request['blue'][0])
        if request['light'][0].lower() == 'a': 
            color.setA(light.ser, red, green, blue)
        elif request['light'][0].lower() == 'b': 
            color.setB(light.ser, red, green, blue)
        elif request['light'][0].lower() == 'ab': 
            color.setA(light.ser, red, green, blue)
            color.setB(light.ser, red, green, blue)
            
    elif 'color' in request: 
        color=request['color'][0]
        if request['light'][0].lower() == 'a': 
            light.colors[color].setA() 
        elif request['light'][0].lower() == 'b': 
            light.colors[color].setB() 
        elif request['light'][0].lower() == 'ab': 
            light.colors[color].setA() 
            light.colors[color].setB() 
    elif 'brightness' in request: 
        color.setW(light.ser, int(request['brightness'][0]))
    
    elif 'off' in request: 
        color.setA(light.ser, 0, 0, 0)
        color.setB(light.ser, 0, 0, 0)
        color.setW(light.ser, 0) 
    elif 'on' in request: 
        color.setA(light.ser, 255, 15, 0)
        color.setB(light.ser, 255, 15, 0)
        color.setW(light.ser, 255)



print '<h1><a href="index.py?off">All Lights off</a></h1>' 

print '<h2>Enter your own RGB color or pick from the list. </h2>'
print '<table> <tr>' 
for set in ['a', 'b', 'w']: 

    # red = 0
    # green = 0
    # blue = 0

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

    print '<form action="index.py" method="post"><input type="hidden" name="light" value="' + set + '"><table>'
    if set in ('a', 'b'): 
        print '<tr><td>Red: </td><td><input type="text" name="red" value=', red, '></td></tr>'
        print '<tr><td>Green: </td><td><input type="text" name="green" value=', green, '></td></tr>' 
        print '<tr><td>Blue: </td><td><input type="text" name="blue" value=', blue, '></td></tr>' 
    else: 
        print '<tr><td>Brightness: </td><td><input type="text" name="brightness" value=', white, '></td></tr>'

    print '<tr><td align="middle"><input type="submit" value="set"></td></tr></table></form>'
    
    if set in ('a', 'b'): 
        print '<form action="index.py" method="post">' 
        print '<input type="hidden" name="light" value="' + set + '">' 
        print '<select name=color>' 
        for col in light.colors: 
            print '<option value="' + col + '">' + col.title() + '</option>'
        print '</select> <input type="submit" value="set"></form>' 

    print '</td>' 
    
print '</tr></table>'

# print '<form action="index.py" method="post"><input type="hidden" name="off" value="">' 
# print '<input type="submit" value="All off"> </form> ' 



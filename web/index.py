import light
import color

print "<h1>RGB Light Control</h1>" 
red="0"
green="0"
blue="0"

if request: 
    if 'red' in request: 
        red=int(request['red'][0])
        green=int(request['green'][0])
        blue=int(request['blue'][0])
        color.set(light.ser, red, green, blue)
    elif 'color' in request: 
        color=request['color'][0]
        light.colors[color].set() 




print '<h2>Enter your own RGB color</h2>'
print '<form action="index.py" method="post"><table>'
print '<tr><td>Red: </td><td><input type="text" name="red" value=', red, '></td></tr>'
print '<tr><td>Green: </td><td><input type="text" name="green" value=', green, '></td></tr>' 
print '<tr><td>Blue: </td><td><input type="text" name="blue" value=', blue, '></td></tr>' 
print '<tr><td align="middle"><input type="submit" value="set"></td></tr></table></form>'

# color.set(light.ser, 255, 200, 100)

print '<h2>Or pick from a list</h2>' 
print '<form action="index.py" method="post">' 
print '<select name=color>' 
for col in light.colors: 
    print '<option value="' + col + '">' + col.title() + '</option>'
print '</select> <input type="submit" value="set"></form>' 



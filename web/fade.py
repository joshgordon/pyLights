import color
import time


exp= 4/3.0
# for i in range(65): 
#     color.setB(light.ser, int(i**exp), int(i**exp), int(i**exp))
#     print i**exp
#     time.sleep(.03)

def fade(ser, fTime, light, start, end): 
    colors = 3
    for i in range(65): 
        current = list() 
        if light.lower() == 'w': 
            colors = 1
        for c in range(colors): 
            if end[c] > start[c]: 
                current.append(int((end[c]-start[c])/256.0 * i ** exp + start[c]))
            else: 
                current.append(int(start[c] - (start[c]-end[c])/255.0 * i ** exp))
                
        if light.lower() == "a":
            color.setA(ser, current[0], current[1], current[2])
        elif light.lower() == "b":
            color.setB(ser, current[0], current[1], current[2])
        elif light.lower() == "w": 
            color.setW(ser, current[0])
            
        time.sleep(fTime/64.0)

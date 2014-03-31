#Defines a single RGB color. Also includes function for setting color based on
# arbitrary RGB values. 
# Written by Josh Gordon (github.com/joshgordon) 
# All code is licensed under the GNU GPL, Version 2 or later. 

import fade

# Sorry for the lack of comments, I kinda threw this together quickly... 

class Color: 
    """A single color"""

    red = 0
    green = 0
    blue = 0

    def __init__(self, red, green, blue): 
        self.red = red
        self.green = green
        self.blue = blue

    def getColor(self): 
        return list(self.red, self.green, self.blue)


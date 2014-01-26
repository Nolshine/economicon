#####################
#                   #
#   MAP GENERATOR   #
#                   #
#####################

# importing important modules

from random import random, choice





"""
This module generates an 16x16 economic map. It makes an 16x16 grid and
iterates over it repeatedly until all gameplay elements from a predefined
list are 'spent' on the playing field. Then it returns the generated map.

PB = Player Base
AA = Alien Artefact
EB = Enemy Base
GD = Gold Deposit
FR = FoRest
DI = DIrt
"""

def generate():
    print "creating assets to be distributed..."
    assets = ["PB",
              "AA",
              "EB",
              "GD",
              "GD",
              "FR",
              "FR",
              "FR"]
    default_asset = "DI"
    size = 16 #desired square size of map
    
    print "creating playfield..."
    field = []
    for i in range(size):
        field.append([])

    print "filling playfield..."
    for y in field:
        for i in range(size):
            y.append(default_asset)

    while assets != []:
        for item in assets:
            while 1:
                y = int(random()*len(field))
                x = int(random()*len(field))
                if field[y][x] != "DI":
                    continue
                break
            field[y][x] = item
            assets.remove(item)
            

##Everything under here is debug messaging
    print "the map looks like:"
    for line in field:
        print_line = ""
        for item in line:
            print_line += "["+item+"]"
        print print_line

    return field

if __name__ == "__main__":
    print "generating 10 maps"
    for i in range(10):
        field = generate()
        print ""
    
    

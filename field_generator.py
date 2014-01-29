# importing important modules
from random import random, choice

#if testing from here, we'll need pygame elements
if __name__ == "__main__":
    import pygame
    from pygame.locals import *
    
#import the Tile class because we need it to generate.   
from entities import Tile

def generate_field(size = 16):
    
    size = size #desired square size of map
    
    print "creating playfield..."
    field = []
    print "populating with dug out dirt..."
    for i in range(size):
        field.append([])
        for n in range(size):
            field[i].append(Tile())
    print "done. (Possibly) creating undug dirt..."
    for row in field:
        for tile in row:
            if random() > 0.7:
                tile.flip()
    print "done."

    return field

if __name__ == "__main__":
    field = generate_field()
    print "This is what it looks like in numbers:"
    for row in field:
        to_print = ""
        for tile in row:
            to_print += ("["+str(tile.is_dug)+"]")
        print to_print
    print "Cells marked [0] are undug cells."
    print "Cells marked [1] are cells that are dug out."
    print "Test complete."

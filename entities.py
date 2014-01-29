import pygame
from pygame.locals import *


class Tile:
    #this is global data, accessible by all instances
    spritesheet = []
    print "loading dirt sprites..."
    #here I load dirt sprites and scale them x2 at the same time
    spritesheet.append(pygame.transform.scale(
        pygame.image.load("dirt_back.png"), (32, 32)))
    spritesheet.append(pygame.transform.scale(
        pygame.image.load("dirt.png"), (32, 32)))
    print "done loading dirt sprites."

    def __init__(self, is_filled = 1):
        self.is_filled = is_filled
        self.sprite = Tile.spritesheet[self.is_filled]

    def flip(self):
        if self.is_filled:
            self.is_filled = 0
            self.sprite = Tile.spritesheet[self.is_filled]
        else:
            self.is_filled = 1
            self.sprite = Tile.spritesheet[self.is_filled]


if __name__ == "__main__":
    tile1 = Tile()
    tile2 = Tile(0)

    pygame.init()

    screen = pygame.display.set_mode((64, 64), DOUBLEBUF)

    clock = pygame.time.Clock()

    #test loop
    try:
        print "Rendering dug (empty) dirt Tile..."
        for i in range(400):
            clock.tick(60)
            pygame.event.pump()
            screen.blit(tile1.sprite, (16, 16))
            pygame.display.update()
        print "Done. Rendering undug (full) dirt Tile./."
        for i in range(400):
            clock.tick(60)
            pygame.event.pump()
            screen.blit(tile2.sprite, (16, 16))
            pygame.display.update()
        pygame.quit()
    except:
        print "exception quit..."
        pygame.quit()
            

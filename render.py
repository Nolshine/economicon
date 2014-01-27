if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    from field.generator import generate
    testfield = generate()



def init_display(field):
    size = len(field)
    size *= 32
    screen = pygame.display.set_mode((size, size), DOUBLEBUF)
    return screen

def render_field(field):
    size = len(field)
    for y in range(size):
        for x in range(len(field)):
            position = (x*32, y*32)
            #below is a test render, showing positioning
            rec = pygame.Rect(position[0], position[1], 32, 32)
            pygame.draw.rect(screen, (255,255,255), rec)
            rec = pygame.Rect(position[0]+1, position[1]+1, 30, 30)
            pygame.draw.rect(screen, (0,0,0), rec)









if __name__ == "__main__":
    pygame.init()
    
    screen = init_display(testfield)

    clock = pygame.time.Clock()

    while 1:
        try:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    raise KeyboardInterrupt
            print "rendering..."
            render_field(testfield)
            pygame.display.flip()
            
        except(KeyboardInterrupt):
            pygame.quit()
            print "done testing"
            break

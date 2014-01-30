if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    from field_generator import generate_field
    testfield = generate_field()



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
            screen.blit(field[y][x].sprite, position)
    pygame.display.update()
            









if __name__ == "__main__":
    pygame.init()
    
    screen = init_display(testfield)

    clock = pygame.time.Clock()
    frames = 0

    while 1:
        try:
            frames += 1
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    raise KeyboardInterrupt
            pygame.display.set_caption("rendering... frames elapsed: "+str(frames))
            render_field(testfield)
            
        except(KeyboardInterrupt):
            pygame.quit()
            print "done testing"
            break

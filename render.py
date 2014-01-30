if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    from field_generator import generate_field



def init_display(field):
    size = 16
    size *= 32
    screen = pygame.display.set_mode((size, size), DOUBLEBUF)
    return screen

def render_field(field, cam_pos):
    screen.fill((0,0,0))
    #iterate through 16 rows...
    for y in range(16):
        #of 16 tiles.
        for x in range(16):
            #position on screen is always between 0*32 and 16*32.
            scr_pos = ((x*32), (y*32))
            #tile pos refers to which tile the camera is on.
            #this is determined outside of the render_field() function.
            posx = cam_pos[0]+x
            posy = cam_pos[1]+y
            #blit the correct tile sprite to screen.
            #tiles determine what their own sprite is.
            screen.blit(field[posy][posx].sprite, scr_pos)
    pygame.display.update()
            









if __name__ == "__main__":
    testfield = generate_field(16*5)
    
    pygame.init()
    
    screen = init_display(testfield)

    clock = pygame.time.Clock()
    frames = 0

    #default camera position currently at (x, y) = (0,0)
    cam_pos = [0, 0]

    while 1:
        try:
            frames += 1
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    raise KeyboardInterrupt
                #testing scrolling with the keyboard.
                #scrolling happens in increments of 1 or 10.
                #this is because I'm working with tiles,
                #and I'm not yet sure how to do smooth
                #tile-scrolling yet.
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        if cam_pos[0] > 0:
                            cam_pos[0] -= 1
                    if event.key == K_d:
                        if cam_pos[0] < (len(testfield))-16:
                            cam_pos[0] += 1
                    if event.key == K_w:
                        if cam_pos[1] > 0:
                            cam_pos[1] -= 1
                    if event.key == K_s:
                        if cam_pos[1] < (len(testfield))-16:
                            cam_pos[1] += 1
            pygame.display.set_caption("rendering... frames: "+str(frames)+" cam: "+str(cam_pos))
            render_field(testfield, cam_pos)
            
        except(KeyboardInterrupt):
            pygame.quit()
            print "done testing"
            break

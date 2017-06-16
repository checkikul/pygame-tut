import pygame

#kicks off all the modules required for PyGame
pygame.init()

#Launches a window of desired size, return value is a Surface object
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): #this empties the event queue, if not used program may become unresponsive 
        if event.type == pygame.QUIT: #event triggered when clicking close window button
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y-=3
    if pressed[pygame.K_DOWN]:
        y+=3
    if pressed[pygame.K_LEFT]:
        x-=3
    if pressed[pygame.K_RIGHT]:
        x+=3

    screen.fill((0,0,0))
    
    if is_blue:
        color = (0,128,255)
    else:
        color = (255,100,0)
    #1st arg - the surface object; 2nd arg - color of the rect; 3rd arg - size of the rect drawn
    pygame.draw.rect(screen, color, pygame.Rect(x,y,60,60))
    #swaps the buffers; i.e it is needed so that any updates on the surface object becomes visible
    pygame.display.flip()
    clock.tick(60)

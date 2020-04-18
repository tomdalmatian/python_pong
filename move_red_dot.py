import pygame, sys, random, time
from pygame.locals import *
pygame.init()
#               R    G    B
WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
GREEN       = (  0, 155,   0)
BLUE        = (  0,   0, 155)
YELLOW      = (155, 155,   0)

pygame.display.set_caption('press q to exit, L-arrow, R-arrow to move')
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
xpos = 50

while True:  #  this is an infinite game loop
    # these 2 somehow get the keyboard input
    pressed_keys = pygame.key.get_pressed()
    pygame.event.get()                     
    # sets the speed
    clock.tick(100)
    # action the keyboard input
    if pressed_keys[K_q]:
        sys.exit()
    if pressed_keys[K_RIGHT]:
        xpos += 1
    if pressed_keys[K_LEFT]:
        xpos -= 1
    # create image
    screen.fill(BLACK)
    pygame.draw.circle(screen,RED,(xpos,200),10)
    # guess what this does!!!
    pygame.display.update()

import pygame, sys, random, time
from pygame.locals import *
pygame.init()
#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

width=1150
height=530
#width=790
#height=480
blue_width=int(width/50)
blue_height=int(height/3)
blue_x=int(width/10)
blue_y=int(height/10)
red_width=int(width/50)
red_height=int(height/3)
red_x=9*int(width/10)
red_y=int(height/10)
bat_speed=3
pygame.display.set_caption('henpong')
screen = pygame.display.set_mode((width,height))
xpos = int(width/2)
ypos= int(height/2)
dot_size=int(height/30)
dot_colour=GREEN
clock = pygame.time.Clock()

xvect=0
while xvect==0:
   print (xvect)
   xvect=random.randint(-6, 6)
yvect=0
while yvect==0:
   print (yvect)
   yvect=random.randint(-6, 6)

print(xvect, yvect)
while 1:
    pressed_keys = pygame.key.get_pressed()
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    xpos += xvect
    ypos += yvect
    if xpos>width or xpos<0:
        xvect=xvect*(-1)
    if ypos<0 or ypos>height:
        yvect = -yvect      
#check for bat hit ...
#blue bat
    if xvect <0: #check going left
        if xpos<=blue_x+blue_width:
            if ypos>blue_y and ypos<blue_y+blue_height:#check bat intersect
                xvect = -xvect
                yvect=yvect+random.randint(-1, 1)
#red bat
    if xvect >0: #check going right
        if xpos>=red_x-red_width:#left right bat loc
            if ypos>red_y and ypos<red_y+red_height:#check bat intersect
                xvect = -xvect
                yvect=yvect+random.randint(-1, 1)
               
    if pressed_keys[K_w]:
        blue_y -= bat_speed
        if blue_y<0:
           blue_y=1
    if pressed_keys[K_s]:
        blue_y += bat_speed
        if blue_y>height-blue_height:
           blue_y=height-blue_height-1
    if pressed_keys[K_UP]:
        red_y -= bat_speed
        if red_y<0:
           red_y=1
    if pressed_keys[K_DOWN]:
        red_y += bat_speed
        if red_y>height-red_height:
           red_y=height-red_height-1

    screen.fill(WHITE)
    pygame.draw.circle(screen,dot_colour,(xpos,ypos),dot_size)
    pygame.draw.rect(screen,BLUE,(blue_x,blue_y,blue_width,blue_height))
    pygame.draw.rect(screen,RED,(red_x,red_y,red_width,red_height))
  #  pygame.draw.rect(screen,RED,(10,10,20,300))
    pygame.display.update()

from itertools import filterfalse

import pygame
from pygame.locals import *

pygame.init()

### Create Window
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python') #set window caption

done = False

while not done:
    #main game loop
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            done = True
    pygame.display.flip() #flip display to 2nd buffer (look back to DOUBLEBUF) keeps us from seeing drawing processes
    pygame.time.wait(100) #makes sure loop pauses for 100 millisec before restarting the loop
pygame.quit()
# CHALLENGE: Plot our star sign Capricorn using openGL drawing


import pygame
from pygame.locals import *

#Bring in OpenGL Libraries
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

###SET UP WINDOW###

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")

#Declare method to set up camera
## orthographic projection
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() # clean pallet
    gluOrtho2D(0, 640, 0, 480) #Set window coordinates. X:0-640 and Y:0-480

# Draw Star
  # reduce amount of times to call glVertex2i
def draw_star(x,y,size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()


done = False
init_ortho() # call camera setup method

### MAIN LOOP ###
while not done:
    # Pygame input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #OpenGL drawing
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear screen (anything to do with color or depth)
    glMatrixMode(GL_MODELVIEW) #set up openGL to start drawing in model coordinate systems
    glLoadIdentity() #clear out what is in the model view
    # glPointSize(10) # so we can see points

    # Draws larger stars
    largerStars = [[150,300], [450,320], [430,300]]
    for s in largerStars:
        draw_star(s[0],s[1],15)

    smallerStars = [[190,250], [230,230], [290,200], [310,220], [420, 285], [280,295], [240,297], [210,299]]
    for s in smallerStars:
        draw_star(s[0],s[1],10)

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
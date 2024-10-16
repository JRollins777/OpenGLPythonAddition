import math
import numpy as np

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

# SCREEN
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')

# ORTHOGRAPHIC VIEW
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-4, 4, -20, 20) # origin is in the center of the screen

# Plots point
# plot f(x) = e^(-x)cos(2pix)
def plot_graph():
    glBegin(GL_POINTS)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(-4,4,0.005):
        py = math.exp(-px) * math.cos(2*math.pi*px)
        glVertex2f(px,py)
    #glVertex2f(1, 1)
    glEnd()

done = False
init_ortho()
glPointSize(5)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_graph()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()

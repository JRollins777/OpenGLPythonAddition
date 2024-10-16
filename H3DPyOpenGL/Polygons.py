import math
import numpy as np

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

## SET UP
pygame.init()

screen_width = 800
screen_height = 800

ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Polygons in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)

def plot_polygon():
    glColor(1, 0, .294, 1)
    glBegin(GL_POLYGON)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()
    glColor(0, 0, 1, 1)
    glBegin(GL_LINE_LOOP)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

# test other glBegin options

# GL_TRIANGLES - makes triangles out of every three points
def triangles():
    glColor(1, 0, .294, 1)
    glBegin(GL_TRIANGLES)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()
    glColor(0, 0, 1, 1)
    for i in np.arange(0,len(points)-2, 3):
        glBegin(GL_LINE_LOOP)
        glVertex2f(points[i][0], points[i][1])
        glVertex2f(points[i+1][0], points[i+1][1])
        glVertex2f(points[i+2][0], points[i+2][1])
        glEnd()

# GL_TRIANGLE_STRIP - first triangle is drawn after 3 points given, then every addition point is added to shape as a vertex
def triangle_strip():
    glColor(1, 0, .294, 1)
    glBegin(GL_TRIANGLE_STRIP)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

# GL_TRIANGLE_FAN - opens like a fan
def triangle_fan():
    glColor(1, 0, .294, 1)
    glBegin(GL_TRIANGLE_FAN)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

# GL_QUADS
def quads():
    glColor(1, 0, .294, 1)
    glBegin(GL_QUADS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

# GL_QUAD_STRIP - draws in counterclockwise order
def quad_strip():
    glColor(1, 0, .294, 1)
    glBegin(GL_QUADS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

def draw_test():
    glColor(1,0,.294,1)
    glBegin(GL_QUAD_STRIP)
    # glVertex2f(-150,250)
    # glVertex2f(150,250)
    # glVertex2f(0, 0)
    for p in points:
        glVertex2f(p[0],p[1])
    glEnd()

    glColor(0, 0, 1, 1)
    glBegin(GL_LINE_LOOP)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

done = False
init_ortho()
points = []
glLineWidth(3)
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                           map_value(0, screen_height, ortho_bottom, ortho_top, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #plot_polygon()
    #draw_test()
    quads()
    pygame.display.flip()
pygame.quit()

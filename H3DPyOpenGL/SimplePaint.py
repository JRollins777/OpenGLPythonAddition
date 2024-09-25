import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import math
import numpy as np

from Utils import *

pygame.init()

screen_width = 800
screen_height = 800

ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_point():
    glBegin(GL_POINTS)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()

def plot_lines():
    for l in points:
        glBegin(GL_LINE_STRIP)
        for cords in l:
            glVertex2f(cords[0], cords[1])
        glEnd()


def save_drawing():
    f = open("drawing.txt", "w")
    f.write(str(len(points)) + "\n") # number of lines in drawing
    for l in points:
        f.write(str(len(l)) + "\n")

        for coords in l:
            f.write(str(coords[0]) + " " + str(coords[1]) + "\n")
    f.close()
    print("Drawing Saved")

def load_drawing():
    f = open("drawing.txt", "r")
    num_of_lines = int(f.readline()) #read one line at a time
    global points
    global line
    points = []
    for l in range(num_of_lines):
        line = []
        points.append(line)
        num_of_coords = int(f.readline())
        for coord_num in range(num_of_coords):
            px, py = [float(value) for value in next(f).split()] # read line and split it in half based on space
            line.append((px,py))
            print(str(px) + "," + str(py))
    print("Drawing Loaded")

def clear_drawing():
    global points
    points = []
    print("Drawing Cleared")


def plot_graph():
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(0,4,0.005):
        py = math.exp(-px) * math.cos(2*math.pi*px)
        glVertex2f(px,py)
    #glVertex2f(1, 1)
    glEnd()

done = False
init_ortho()
glPointSize(5)
points = []
line = []
mouse_down = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_drawing()
            elif event.key == pygame.K_l:
                load_drawing()
            elif event.key == pygame.K_SPACE:
                clear_drawing()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
            line = []
            points.append(line)
        elif event.type == MOUSEBUTTONUP:
            mouse_down= False
        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            line.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                           map_value(0,screen_height, ortho_bottom, ortho_top, p[1]))) # if mouse clicked then p holds the position of mouse when clicked

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_lines()
    #plot_graph()
    pygame.display.flip()
    #pygame.time.wait(100)
pygame.quit()

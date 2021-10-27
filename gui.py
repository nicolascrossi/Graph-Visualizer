from typing import Dict, List
import pygame
from node import Node
from collections import defaultdict

from algorithms import *

#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Screen height and width
S_HEIGHT = 900
S_WIDTH = 1000

# Number of nodes to fit in the screen
NODES = 100

dim = (S_WIDTH // NODES, S_HEIGHT // NODES)

nodes: List[List[Node]] = []

for i in range(NODES):
    lst = []
    for k in range(NODES):
        lst.append(Node(dim, 1, BLUE))
    nodes.append(lst)

for r_i, row in enumerate(nodes):
    for c_i, node in enumerate(row):
        if c_i > 0:
            # node.left = (row[c_i - 1], 1)
            node.left = row[c_i - 1]
        if c_i < NODES - 1:
            # node.right = (row[c_i + 1], 1)
            node.right = row[c_i + 1]
        if r_i > 0:
            # node.up = (nodes[r_i - 1][c_i], 1)
            node.up = nodes[r_i - 1][c_i]
        if r_i < NODES - 1:
            # node.down = (nodes[r_i + 1][c_i], 1)
            node.down = nodes[r_i + 1][c_i]

root = nodes[0][0]

pygame.init() #start pygame

screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

pygame.display.set_caption('Pygame')

clock = pygame.time.Clock()

done = False

start: Node | None = None
goal: Node | None = None
s_down = False
g_down = False

stepping = False

q = prev = None

while not done:
    for event in pygame.event.get(): #check the events list
        if event.type == pygame.QUIT: #if the user clicks the X
            done = True #now we're done displaying
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:
                for row in nodes:
                    for node in row:
                        if node.inside(event.pos):
                            node.color = RED
                            node.weight = 1000
                            if node == goal:
                                goal = None
                            elif node == start:
                                start = None
            elif event.buttons[2]:
                for row in nodes:
                    for node in row:
                        if node.inside(event.pos):
                            node.color = BLUE
                            node.weight = 1
                            if node == goal:
                                goal = None
                            elif node == start:
                                start = None
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for row in nodes:
                    for node in row:
                        if node.inside(event.pos):
                            if s_down:
                                if start:
                                    start.color = BLUE
                                start = node
                                node.color = GREEN
                            elif g_down:
                                if goal:
                                    goal.color = BLUE
                                goal = node
                                goal.color = WHITE
                            else:
                                node.color = RED
                                node.weight = 1000
                                if node == goal:
                                    goal = None
                                elif node == start:
                                    start = None
            elif event.button == 3:
                for row in nodes:
                    for node in row:
                        if node.inside(event.pos):
                            if s_down:
                                if start:
                                    start.color = BLUE
                                start = node
                                node.color = GREEN
                            elif g_down:
                                if goal:
                                    goal.color = BLUE
                                goal = node
                                goal.color = WHITE
                            else:
                                node.color = BLUE
                                node.weight = 1
                                if node == goal:
                                    goal = None
                                elif node == start:
                                    start = None

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                s_down = True
            elif event.key == pygame.K_g:
                g_down = True

            if event.key == pygame.K_q:
                if start and goal:
                    stepping = True
            
            if event.key == pygame.K_r:
                for row in nodes:
                    for node in row:
                        node.color = BLUE
                        start = None
                        goal = None
                        node.weight = 1

            if event.key == pygame.K_SPACE:
                if start and goal:
                    # INSERT FUNCTION HERE
                    bfs(start, goal)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                s_down = False
            elif event.key == pygame.K_g:
                g_down = False

    screen.fill(BLACK)

    if stepping:
        if q is None and prev is None:
            q, prev = bfs_step_setup(start)
        
        if bfs_step(q, prev, goal):
            trail(prev, goal, start)
            q = None
            prev = None
            stepping = False

    x = 0
    y = 0

    for row in nodes:
        for node in row:
            node.draw(screen, (x, y))
            y += dim[1]
        x += dim[0]
        y = 0

    

    pygame.display.update()

    clock.tick(60)
#-*- coding: utf-8 -*-
from random import *
from string import *
import drawer
import sys
import pdb

h = 30
mx = 22
my = 22
imgx = mx * h
imgy = my * h

f = open('maze.txt', 'w')

stack = []
maze = [[0 for x in range(mx * my)] for y in range(mx * my)]
visited = [[0 for x in range(mx)] for y in range(my)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def count_index(x, y):
    return y * my + x

def visit(x, y):
    if len(stack) > 0:
        visited[y][x] = 1
        avail = []
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if newy < my and newy >= 0 and newx < mx and newx >= 0:
                if visited[newy][newx] == 0:
                    avail.append(i)
        next_pos = None
        if len(avail) == 0:  # никуда не можем пойти, значит это тупик
            next_pos = stack.pop()  # идем назад
        else:
            dest = avail[randrange(len(avail))]
            next_pos = (x + dx[dest], y + dy[dest])

            index = count_index(next_pos[0], next_pos[1])
            prev_index = count_index(x, y)
            maze[index][prev_index] = 1
            maze[prev_index][index] = 1
            stack.append(next_pos)
        visit(next_pos[0], next_pos[1])


startx = randrange(mx)
starty = randrange(my)
stack.append((startx, starty))
visit(startx, starty)

for row in maze:
    for cell in row:
        f.write(str(cell))
    f.write('\n')

drawer = drawer.Drawer(h, mx, my)
drawer.draw(maze)
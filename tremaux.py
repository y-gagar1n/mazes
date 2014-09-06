#-*- coding: utf-8 -*-
from random import *
from string import *
import sys
from solver import Solver

h = 30
mx = 40
my = 40

filename = 'maze_' + str(mx) + 'x' + str(my) + '.txt'
f = open(filename, 'r')
maze = [[int(a) for a in list(line.strip())] for line in f.readlines()]

stack = []
visited = [[0 for x in range(mx)] for y in range(my)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def count_index(x, y):
    return y * my + x

def get_avail(x, y):
    avail = []
    for i in range(len(dx)):
        newx = x + dx[i]
        newy = y + dy[i]
        if newy < my and newy >= 0 and newx < mx and newx >= 0:
            if visited[newy][newx] == 0 and maze[count_index(newx, newy)][count_index(x,y)]:
                avail.append(i)
    return avail


def visit(x, y):
    if x == mx-1 and y == my-1: return True
    if len(stack) > 0:
        visited[y][x] = 1
        avail = get_avail(x, y)
        while len(avail) > 0:
            next_pos = None
            if len(avail) == 0:  # никуда не можем пойти, значит это тупик
                next_pos = stack.pop()  # идем назад
            else:
                dest = avail[randrange(len(avail))]
                next_pos = (x + dx[dest], y + dy[dest])

                index = count_index(next_pos[0], next_pos[1])
                prev_index = count_index(x, y)

                stack.append(next_pos)
                if(visit(next_pos[0], next_pos[1])): return True
            avail = get_avail(x, y)
        stack.pop()
    return False


startx = 0
starty = 0
stack.append((startx, starty))
visit(startx, starty)

solver = Solver(h, mx, my)
solver.draw(maze, stack)

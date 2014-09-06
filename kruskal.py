#-*- coding: utf-8 -*-
import random
import drawer

h = 10
mx = 10
my = 10

f = open('maze.txt', 'w')

graph = [[0 for x in range(mx * my)] for y in range(mx * my)]

def get_index((x,y)):
    return y * mx + x

edges = []
for y in range(my):
    for x in range(mx):
        if x > 0: edges.append((y,x,'S'))
        if y > 0: edges.append((y,x,'E'))
random.shuffle(edges)

sets = []
maze = [[y * mx + x for x in range(mx)] for y in range(my)]
for y in range(my):
    for x in range(mx):
        sets.append([(y, x)])

sets_n = mx * my

while sets_n > 1:    
    edge = edges.pop()
    dest = edge[2]
    cell1 = None; cell2 = None
    if dest == 'S': 
        cell1 = (edge[0], edge[1] -1)
        cell2 = (edge[0], edge[1])
    if dest == 'E':
        cell1 = (edge[0] - 1, edge[1])
        cell2 = (edge[0], edge[1])
    n1 = maze[cell1[0]][cell1[1]]
    n2 = maze[cell2[0]][cell2[1]]
    if not n1 == n2:
        i1 = get_index(cell1)
        i2 = get_index(cell2)
        graph[i1][i2] = 1
        graph[i2][i1] = 1
        set1 = sets[n1]
        set2 = sets[n2]
        for item in set2:
            set1.append(item)
            maze[item[0]][item[1]] = n1
        sets[n1] = set1
        sets[n2] = []
        sets_n -= 1

for row in graph:
    for cell in row:
        f.write(str(cell))
    f.write('\n')

drawer = drawer.Drawer(h, mx, my)
drawer.draw(graph)
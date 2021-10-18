from math import sqrt

class Node:

    def __init__ (self):
        self.f = 0

def aStarPathfinding (m):
    openSet = []
    closedSet = []
    sideLength = len(m)

    startingNode = -1
    for y in len(m):
        for x in len(m[y]):
            if m[y][x] == 2:
                startingNode = sideLength * y + x
    
    openSet.append(startingNode)
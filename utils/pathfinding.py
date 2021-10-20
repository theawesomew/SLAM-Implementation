from math import sqrt
import time

# create a new node class to store information needed for
# the A* pathfinding algorithm to function
class Node:

    def __init__ (self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__ (self, other):
        return self.position == other.position

# This is an implementation of the A* pathfinding algorithm
# This algorithm was developed by Peter Hart, Nils Nilsson, & Bertram Raphael in 1968 as part of the
# Shakey project. 
# This utilises best-search first algorithm which looks at the "cost" of traversing along a particular node
# as a function of how far away it is from both the starting node & the goal node.
# This relationship can be defined mathematically as f(n) = g(n) + h(n)
# where g(n) is the "cost" of making it to this node & h(n) is the heuristic function which
# uses the pythagorean theorem a**2 + b**2 = c**2 to estimate the future cost of that node

matrix = [[2, 0, 0, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 1, 1, 3],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 1, 3]]

def aStarPathfinding (m):
    openSet = []
    closedSet = []
    sideLength = len(m)

    startingNode = -1
    endingNode = -1
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == 2:
                startingNode = Node(None, [x, y])
                startingNode.f = startingNode.g = startingNode.h = 0
            elif m[y][x] == 3:
                endingNode = Node(None, [x, y])
                endingNode.f = endingNode.g = endingNode.h = 0
    
    openSet.append(startingNode)   

    while len(openSet) > 0:
        currentNode = openSet[0]
        currentIndex = 0

        for index, item in enumerate(openSet):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        openSet.pop(currentIndex)
        closedSet.append(currentNode)

        if currentNode == endingNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nodePosition = [currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1]]

            if nodePosition[0] > len(m) - 1 or nodePosition[0] < 0 or nodePosition[1] > len(m) - 1 or nodePosition[1] < 0:
                continue

            if m[nodePosition[1]][nodePosition[0]] != 0 and m[nodePosition[1]][nodePosition[0]] != 3:
                continue

            newNode = Node(currentNode, nodePosition)

            if newNode in closedSet:
                continue
            
            children.append(newNode)

        for child in children:

            for closedChild in closedSet:
                if closedChild == child:
                    continue

            child.g = currentNode.g + 1
            child.h = sqrt((child.position[0]-endingNode.position[0])**2 + (child.position[1]-endingNode.position[1])**2)
            child.f = child.g + child.h

            for openNode in openSet:
                if child == openNode and child.g > openNode.g:
                    continue

            openSet.append(child)

# This code takes the path generated by the A* search algorithm & returns the formatted
# "follow string" which the robot can then use to direct itself by
def generateFollowString (path):
    result = ""

    for i in range(1,len(path)):
        currentX, prevX, = path[i][0], path[i-1][0]
        currentY, prevY, = path[i][1], path[i-1][1]

        if prevX - currentX == -1:
            result += "R"
        elif prevX - currentX == 1:
            result += "L"
        else:
            result += ""

        if prevY - currentY == -1:
            result += "B"
        elif prevX - currentX == 1:
            result += "F"
        else:
            result += ""

    return result

print(aStarPathfinding(matrix))
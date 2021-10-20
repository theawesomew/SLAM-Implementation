from math import sqrt

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

            if nodePosition[0] > len(m) - 1 or nodePosition[0] < 0 or nodePosition[1] > len(m[len(m)-1])-1 or nodePosition[1] < 0:
                continue

            if m[nodePosition[1]][nodePosition[0]] != 0 and m[nodePosition[1]][nodePosition[0]] != 3:
                continue

            newNode = Node(currentNode, nodePosition)
            
            children.append(newNode)

        for child in children:

            for closedChild in closedSet:
                if closedChild == child:
                    continue

            child.g = currentNode.g + 1
            child.h = (child.position[0]-endingNode.position[0])**2 + (child.position[1]-endingNode.position[1])**2
            child.f = child.g + child.h

            for openNode in openSet:
                if child == openNode and child.g > openNode.g:
                    continue

            openSet.append(child)

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
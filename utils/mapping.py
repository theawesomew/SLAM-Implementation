from math import sqrt

# This is string representation of the environment surrounding the robot
# 1's represent impermeable obstacles
# 0's represent free space
# This map string is generated by a visualisation tool in utils/environment/index.html

# This parses the map string & converts it into an NxN matrix
def parseMapData (str):
    MAP = []

    # compute the side-length of the map as a function of the mapstring's length
    # all maps are square & therefore are suited to the map string representation without
    # the need to input a dimension
    sideLength = int(sqrt(len(str)))

    # iterate through the string & construct a matrix
    for i in range(sideLength):
        # append a new list for every row
        MAP.append([])
        for j in range(sideLength):
            # input the digit at position (x,y) if this string were interpreted as a list of co-ordinates
            # this is done simply by multiplying the y-value by the side-length & adding the x-value
            MAP[i].append(int(str[i*sideLength+j]))
    
    return MAP

# this places the target position in the matrix map representation
def placeTarget (m, x, y):
    if x >= len(m) or y >= len(m): return
    m[y][x] = 3

# this places the robot in the matrix map representation
def placeRobot (m, x, y):
    if x >= len(m) or y >= len(m): return
    m[y][x] = 2 

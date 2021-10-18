from math import sqrt

MAP_STRING = "100010100"

def parseMapData (str):
    MAP = []

    sideLength = int(sqrt(len(str)))

    for i in range(sideLength):
        MAP.append([])
        for j in range(sideLength):
            MAP[i].append(int(str[i*sideLength+j]))
    
    return MAP

def placeTarget (m, x, y):
    if x >= len(m) or y >= len(m): return
    m[y][x] = 2

def placeRobot (m, x, y):
    if x >= len(m) or y >= len(m): return
    m[y][x] = 3 

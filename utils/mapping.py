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

print(len(parseMapData(MAP_STRING)[0]))
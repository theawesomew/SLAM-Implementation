from utils.robot import *
from utils.mapping import *
from utils.pathfinding import *
from utils.vision import *
import time


robot = Robot(0, 0, 0)

MAP_STRING = ""

MAP_MATRIX = parseMapData(MAP_STRING)

placeRobot(MAP_MATRIX, robot.x, robot.y)

placeTarget(MAP_MATRIX, 0, 0)

fString = generateFollowString(aStarPathfinding(MAP_MATRIX))

while True:
    robot.follow(fString)
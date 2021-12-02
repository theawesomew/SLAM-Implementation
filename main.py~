from utils.robot import *
from utils.mapping import *
from utils.pathfinding import *
import time

robot = Robot(0, 0, 90)

MAP_STRING = ""

MAP_MATRIX = parseMapData(MAP_STRING)

placeRobot(MAP_MATRIX, robot.x, robot.y)

placeTarget(MAP_MATRIX, 0, 0)

try:
    robot.follow("F")
    robot.stop()
except KeyboardInterrupt:
    robot.stop()
    print("Program terminated")

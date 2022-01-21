from utils.robot import *

robot = Robot(0,0,90)

try:
    robot.follow("F")
    robot.stop()
except KeyboardInterrupt:
    robot.stop()
    print("Test terminated")

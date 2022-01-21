from utils.robot import *
import time

robot = Robot(0,0,90)

try:
    robot.turn(True)
    time.sleep(1)
    robot.stop()
except KeyboardInterrupt:
    robot.stop()
    print("Test terminated")

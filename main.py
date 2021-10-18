from utils.robot import *
import time


robot = Robot(10, 10, 0)

while True:
    robot.forward(0.5)
    time.sleep(1)
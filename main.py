from utils.robot import *
from utils.mapping import *
from utils.pathfinding import *
from utils.vision import *
import time


robot = Robot(0, 0, 0)
vision = Vision()

while True:
    print(vision.getData())
    
    
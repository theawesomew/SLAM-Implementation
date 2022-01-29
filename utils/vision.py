from json.encoder import INFINITY
import pyrealsense2 as rs

class Vision:

    def __init__ (self):
        self.pipeline = rs.pipeline()
        self.pipeline.start()

    def withinRange (self, range):
        frame = self.pipeline.wait_for_frames()
        width, height = frame.get_width(), frame.get_height()
        depth = frame.get_depth_frame()

        minDistance = INFINITY
        for x in range(width):
            for y in range(height):
                minDistance = min(depth.get_distance(x,y), minDistance)

        if minDistance <= range:
            return True
        else:
            return False

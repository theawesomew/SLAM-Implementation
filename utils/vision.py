import pyrealsense2 as rs
import numpy as np

class Vision:

    def __init__ (self):
        self.pipeline = rs.pipeline()
        self.pipeline.start()

    def getData (self):
        frames = self.pipeline.wait_for_frames()
        depth = frames.get_depth_frame()
        depth_data = depth.as_frame().get_data()
        np_image = np.asanyarray(depth_data)

        return np_image

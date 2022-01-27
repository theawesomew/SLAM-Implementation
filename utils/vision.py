import pyrealsense2 as rs

class Vision:

    def __init__ (self):
        self.pipeline = rs.pipeline()
        self.pipeline.start()
        self.run()

    def run (self):
        while True:
            self.frames = self.pipeline.wait_for_frames()
            self.depth = self.frames.get_depth_frame()
        

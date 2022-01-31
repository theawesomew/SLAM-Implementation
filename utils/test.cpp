#include <iostream>
#include "/home/librealsense/include/librealsense2/rs.hpp"

int main () {

    rs2::pipeline p;

    p.start();

    while (true) {
        rs2::frameset frames = p.wait_for_frames();
        rs2::depth_frame depth_frame = frames.get_depth_frame();

        int width = depth_frame.get_width(), height = depth_frame.get_height();

        float distance_to_centre = depth_frame.get_distance(width/2, height/2);

        std::cout << distance_to_centre << std::endl;
    }

    return 0;
}

#include <iostream>
#include <librealsense2/rs.hpp>

int main () try {

    rs2::pipeline p;

    p.start();

    while (true) {
        rs2::frameset frames = p.wait_for_frames();
        rs2::depth_frame depth_frame = frames.get_depth_frame();

        int width = depth_frame.get_width(), height = depth_frame.get_height();

        float distance_to_centre = depth_frame.get_distance(width/2, height/2);

        std::cout << distance_to_centre << std::endl;
    }

    return EXIT_SUCCESS;
}
catch (const rs2::error & e)
{
    std::cerr << "RealSense error calling " << e.get_failed_function() << "(" << e.get_failed_args() << "):\n    " << e.what() << std::endl;
    return EXIT_FAILURE;
}
catch (const std::exception& e)
{
    std::cerr << e.what() << std::endl;
    return EXIT_FAILURE;
}
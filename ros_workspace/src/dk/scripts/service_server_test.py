#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty, EmptyResponse

class RobotServer:
    def __init__(self):
        rospy.init_node('robot_server')
        rospy.Service('move_robot', Empty, self.move_robot)
        rospy.loginfo("Robot server ready to receive requests.")

    def move_robot(self, request):
        # In a real implementation, you would control the robot's movement here.
        # For demonstration purposes, let's print a message.
        rospy.loginfo("Robot moving forward.")
        return EmptyResponse()

if __name__ == "__main__":
    server = RobotServer()
    rospy.spin()


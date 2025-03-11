#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty

class RobotClient:
    def __init__(self):
        rospy.init_node('robot_client')
        rospy.loginfo("Waiting for service /move_robot...")
        rospy.wait_for_service('/move_robot')
        self.move_robot_service = rospy.ServiceProxy('/move_robot', Empty)

    def move_forward(self):
        rospy.loginfo("Sending request to move the robot forward.")
        try:
            response = self.move_robot_service()
            rospy.loginfo("Robot moved forward successfully.")
        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: %s" % e)

if __name__ == "__main__":
    client = RobotClient()
    client.move_forward()


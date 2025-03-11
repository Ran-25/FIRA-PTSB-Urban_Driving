#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_srvs.srv import Empty, EmptyResponse

def client_yolo():

    rospy.wait_for_service('client_yolo')
    try:
        client_yolo_task = rospy.ServiceProxy('client_yolo', Empty)

        return
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


if __name__ == '__main__':
    client_yolo()


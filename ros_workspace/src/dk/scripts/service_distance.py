#!/usr/bin/env python3
import rospy
import time
from rospy import loginfo
from std_msgs.msg import Float32, String, Byte, Int8
from std_srvs.srv import Empty, EmptyRequest

from donkey_service.srv import DistanceData

class RobotClient:
    def __init__(self):
        rospy.init_node('robot_client')
        rospy.loginfo("Waiting for service /Service_TwistDk...")
        rospy.loginfo("Sending request to move the robot forward.")
        rospy.wait_for_service('/Service_TwistDk')
        self.Service_TwistDk_service = rospy.ServiceProxy('/Service_TwistDk', DistanceData)

        self.detected = None
        self.distance = None
        self.sub_dist = rospy.Subscriber('/detect_dist', Float32, self.detect)
        self.sub_detect = rospy.Subscriber('/detect', String, self.detected_labels)
        self.detect_pub = rospy.Publisher('/detect_signboard', String, queue_size=10)

    def detected_labels(self, data):
        self.detected = data.data

    def detect(self,data):
        self.distance = data.data
#        loginfo('Roboclient.detect()')

        try:
            response = self.Service_TwistDk_service()
            loginfo(response.datarequest.data)
#            rospy.loginfo("Robot moved forward successfully.")
            if self.distance <= 14.9:
                
                if 'stop' in self.detected:
                    loginfo("stop kot")
                    self.detect_pub.publish('stop')

                elif 'dead end' in self.detected:
                    self.detect_pub.publish('dead end')

                elif 'no entry' in self.detected:
                    self.detect_pub.publish('no entry')

                elif 'left' in self.detected:
                    loginfo("left kot")
                    self.detect_pub.publish('left')

                elif 'right' in self.detected:
                    self.detect_pub.publish('right')

                elif 'forward' in self.detected:
                    self.detect_pub.publish('forward')

                else:
                    print('noooo')
                    #self.detect_pub.publish('None')
        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: %s" % e)


if __name__ == "__main__":
#    rospy.init_node('distance_node')
#    control = Distance()
#    rospy.spin()
    client = RobotClient()
#    client.move_forward()
    rospy.spin()

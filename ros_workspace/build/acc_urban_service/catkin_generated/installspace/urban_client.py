#!/usr/bin/env python3
import rospy
import time
from rospy import loginfo
from std_msgs.msg import Float32, String, Byte, Int8
from std_srvs.srv import Empty, EmptyRequest

from acc_urban_service.srv import *

from geometry_msgs.msg import Twist

Twist_pub = rospy.Publisher('/cmd_velDK', Twist, queue_size=1)

def left_move(): #ID dalam detection adalah = 0
    loginfo('left_move')
    twist = Twist()
    twist.linear.x = -0.2

    twist.angular.z = 1.0
    Twist_pub.publish(twist)
    return twist

def right_move():
    loginfo('right_move')
    twist = Twist()
    twist.linear.x = 1

    twist.angular.z = - 1.0
    Twist_pub.publish(twist)

    return twist

class DistanceClient:
    def __init__(self):
        rospy.init_node('service_client_distance')
        rospy.loginfo("Waiting for service /twistdk_service_server...")
        rospy.loginfo("Sending request from node/service service_client_distance")
        self.detected = None
        self.distance = None
        rospy.wait_for_service('twistdk_service')
        self.Service_TwistDk_service = rospy.ServiceProxy('twistdk_service', YoloData, self.get_callback)

    def get_callback(self):
        
        try:
            self.sub_dist = rospy.Subscriber('/detect_dist', Float32, self.detect)
            self.sub_detect = rospy.Subscriber('/detect', Int8, self.sub_detect_func)
            loginfo("Service TwistDk response.")
            loginfo('Roboclient.detect()')
            loginfo('from get_callback(): '+ str(self.detected))
            print(self.distance)
            left_move()
            rospy.sleep(3)
            right_move()
            rospy.sleep(3)
#            d = self.detected if self.detected is None else int(7)
#            req = DistanceDataRequest(request)
#            req.dataresponse.data = request
#            response = self.Service_TwistDk_service(request)
#            d = int(90)
            d = self.detected
            response = self.Service_TwistDk_service.call(YoloDataRequest(d))
#            print(type(response))
#            loginfo(response.dataresponse)
#            print(dir(response))
            return response.datarequest

        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: %s" % e)

    def detect(self, data):
        self.distance = data.data
#        loginfo(self.distance)

    def sub_detect_func(self, data):
        d = data.data
        self.detected = d if isinstance(d, str) else int(d)
#        loginfo(self.detected)
#        print(d)
#        print(type(d))

def main():
    client = DistanceClient()
    rospy.Rate(1.)
    while not rospy.is_shutdown():
        client.get_callback()
#        rospy.sleep(1)


if __name__ == "__main__":
    main()
    rospy.spin()

'''
#        self.detect_pub = rospy.Publisher('/detect_signboard', String, queue_size=10)

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
'''

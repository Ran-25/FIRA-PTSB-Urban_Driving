#!/usr/bin/env python3
import rospy
import time
from rospy import loginfo
from std_msgs.msg import Float32, String, Byte, Int8
from std_srvs.srv import Empty, EmptyRequest

from donkey_service.srv import *


class DistanceClient:
    def __init__(self):
        rospy.init_node('service_client_distance')
        rospy.loginfo("Waiting for service /twistdk_service_server...")
        rospy.loginfo("Sending request from node/service service_client_distance")
        self.detected = None
        self.distance = None
        self.sub_dist = rospy.Subscriber('/detect_dist', Float32, self.detect)
        self.sub_detect = rospy.Subscriber('/detect', String, self.detected_labels)
#        self.detect_pub = rospy.Publisher('/detect_signboard', String, queue_size=10)
        rospy.wait_for_service('twistdk_service')
        self.Service_TwistDk_service = rospy.ServiceProxy('twistdk_service', DistanceData, self.get_callback)

    def get_callback(self):
        
        try:
            loginfo("Service TwistDk response.")
            loginfo('Roboclient.detect()')
            request = repr(self.detected)
#            loginfo('from get_callback(): '+ str(self.detected))
            print(type(request))
#            loginfo(request)
#            req = DistanceDataRequest(request)
#            req.dataresponse.data = request

            response = self.Service_TwistDk_service(request)
#            response = self.Service_TwistDk_service.call(DistanceDataRequest(d))
            print(type(response))
            loginfo(response.dataresponse)
            return response.dataresponse

        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: %s" % e)

    def detect(self, data):
        self.distance = data.data
#        loginfo(self.distance)

    def detected_labels(self, data):
        self.detected = str.encode(data.data)
#        print(self.detected)
#        loginfo('from detected_labels(): '+ str(self.detected))
#        print(type(self.detected))


if __name__ == "__main__":
    client = DistanceClient()
    client.get_callback()
    rospy.spin()

'''

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

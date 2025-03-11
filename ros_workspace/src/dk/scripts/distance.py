#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import Float32, String, Byte, Int8

class Distance():
    def __init__(self):
        self.detected = None
        self.distance = None
        self.sub_dist = rospy.Subscriber('/detect_dist', Float32, self.detect)
#        self.sub_detect = rospy.Subscriber('/detect', Byte, self.detected_labels)
        self.sub_detect = rospy.Subscriber('/detect', String, self.detected_labels)
        self.detect_pub = rospy.Publisher('/detect_signboard', String, queue_size=10)
    
    def detected_labels(self, data):
        self.detected = data.data

    def detect(self,data):
        self.distance = data.data

        if self.distance >= 14.9:
            
            if 'stop' in self.detected:
                print("stop kot")
                self.detect_pub.publish('stop')

            elif 'dead end' in self.detected:
                self.detect_pub.publish('dead end')

            elif 'no entry' in self.detected:
                self.detect_pub.publish('no entry')

            elif 'left' in self.detected:
                print("left kot")
                self.detect_pub.publish('left')
                time.sleep(0.3)

            elif 'right' in self.detected:
                self.detect_pub.publish('right')

            elif 'forward' in self.detected:
                self.detect_pub.publish('forward')

            else:
                print('noooo')
                #self.detect_pub.publish('None')

if __name__ == "__main__":
    rospy.init_node('distance_node')
    control = Distance()
    rospy.spin()

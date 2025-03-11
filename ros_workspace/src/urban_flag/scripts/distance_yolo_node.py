#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import Float32, Int8, Bool


class Distance():
    def __init__(self):
        self.detected = 0
        self.distance = 0.0
        self.sub_dist = rospy.Subscriber('/detect_dist', Float32, self.detect)
        self.sub_detect = rospy.Subscriber('/detect', Int8, self.detected_labels)
        self.detect_pub = rospy.Publisher('/detect_signboard', Int8, queue_size=10)
        self.detect_bool_pub = rospy.Publisher('/detect_bool', Bool, queue_size=10)


    def detected_labels(self, data):
        self.detected = data.data

    def detect(self, data):
        self.distance = data.data

        if self.distance <= 14.9:
            if self.detected == 7:
                rospy.loginfo("No objects detected")
                self.detect_bool_pub.publish(False)

            else:
                rospy.loginfo("Objects detected")
                self.detect_bool_pub.publish(True)
                self.detect_pub.publish(self.detected)
            
        #     if 'stop' in self.detected:
        #         print("stop kot")
        #         self.detect_pub.publish('stop')

        #     elif 'dead end' in self.detected:
        #         self.detect_pub.publish('dead end')

        #     elif 'no entry' in self.detected:
        #         self.detect_pub.publish('no entry')

        #     elif 'left' in self.detected:
        #         print("left kot")
        #         self.detect_pub.publish('left')
        #         time.sleep(0.3)

        #     elif 'right' in self.detected:
        #         self.detect_pub.publish('right')

        #     elif 'forward' in self.detected:
        #         self.detect_pub.publish('forward')

        #     else:
        #         print('noooo')
        #         #self.detect_pub.publish('None')

if __name__ == "__main__":
    rospy.init_node('distance_yolo_node')
    control = Distance()
    rospy.spin()

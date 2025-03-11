#!/usr/bin/env python3
import rospy
from rospy import loginfo
from std_msgs.msg import Int8
from geometry_msgs.msg import Twist

'''
main task/file
detect_sub = rospy.Subscriber('/detect', Int8, detect)

init as variable self.detect_sub=None

use as detect(self.detect_sub)
'''

def detect(data):
    Twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    signboard = data
    
    if signboard == 2:
        print("stop lahh")
        twist = Twist()
        twist.linear.x = -0.5 #throotle value 310 
        twist.linear.y = 0
        twist.linear.z = 0

        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0.02  # steering tegak

        Twist_pub.publish(twist)

    if signboard == 3:
        print("no entry lahh")
        twist = Twist()
        twist.linear.x = -0.5 #throotle value 310 
        twist.linear.z = 0

        twist.angular.x = 0
        twist.angular.z = 0
        Twist_pub.publish(twist)

    if signboard == 4:
        print("dead end lahh")
        twist = Twist()
        twist.linear.x = -0.5 #throotle value 310 
        twist.linear.z = 0

        twist.angular.x = 0
        twist.angular.z = 2.0
        Twist_pub.publish(twist)

    if signboard == 0:
        twist = Twist()
        twist.linear.x = -0.2
        twist.linear.z = 0

        twist.angular.x = 0
        twist.angular.z = 2.0
        Twist_pub.publish(twist)

    if signboard == 2:
        twist = Twist()
        twist.linear.x = 1
        twist.linear.z = 0

        twist.angular.x = 0
        twist.angular.z = - 2.0
        Twist_pub.publish(twist)

    if signboard == 5:
        loginfo('depan')
        twist = Twist()
        twist.linear.x = 1
        twist.linear.z = 0

        twist.angular.x = 0
        twist.angular.z = 0
        Twist_pub.publish(twist)

    return 

'''
detect_sub = rospy.Subscriber('/detect', Int8, detect)

if __name__ == "__main__":
    rospy.init_node('yolo')
#    rospy.spin
'''


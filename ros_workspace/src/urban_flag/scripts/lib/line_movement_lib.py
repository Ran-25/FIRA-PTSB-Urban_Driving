#!/usr/bin/env python3
import rospy
from rospy import loginfo
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8



# data from yolo (degree)
def follow_move(data):
    twist = Twist()
    twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 

    if isinstance(data, type(None)):
        degree_val = 0
    degree_val = data

    # print(type(degree_val))
    if degree_val == 5 and -5:
        loginfo('steering in normal position')

        twist.linear.x = 0.0

        twist.angular.z = 0.02

        twist_pub.publish(twist)

     #positif kamera ke kiri adjust steering ke kanan
    elif degree_val >= 10:
        print(type(degree_val))
        loginfo('steering in normal position')
        # twist = Twist()
        twist.linear.x = 0.0

        twist.angular.z = - 0.3
        twist_pub.publish(twist)
    
    elif degree_val <= -10:
        loginfo('steering in normal position')
        # twist = Twist()
        twist.linear.x = 0.0

        twist.angular.z = 0.3
        twist_pub.publish(twist)
    
    elif degree_val >= 15:
        loginfo('steering in normal position')
        twist = Twist()
        twist.linear.x = 0.0

        twist.angular.z = - 0.8
        twist_pub.publish(twist)

    
    elif degree_val <= - 15:
        loginfo('steering in normal position')
        # twist = Twist()
        twist.linear.x = 0.0

        twist.angular.z = 0.8
        twist_pub.publish(twist)
    
    elif degree_val >= 20:
        loginfo('steering in normal position')
        # twist = Twist()
        twist.linear.x = 0.0

        twist.angular.z = -1.5
        twist_pub.publish(twist)
    
    elif degree_val <= - 20:
        loginfo('steering in normal position')
        # twist = TwistS()
        twist.linear.x = 0.0

        twist.angular.z = 1.5
        twist_pub.publish(twist)

    twist_pub.publish(twist)

    return 


# if __name__ == "__main__":
#     rospy.init_node('test_followLine')
#     # rospy.Rate(10)
#     follow_move(15)

'''f
if __name__ == "__main__":
    rospy.init_node('followLine')
    degree_sub = rospy.Subscriber('/degree_vel', Int8, follow_move)
#    rospy.spin
'''

#!/usr/bin/env python3
import rospy
from rospy import loginfo
from geometry_msgs.msg import Twist

Twist_pub = rospy.Publisher('/cmd_velDK', Twist, queue_size=1)

def left_move(): #ID dalam detection adalah = 0
    twist = Twist()
    twist.linear.x = -0.2

    twist.angular.z = 1.0
    Twist_pub.publish(twist)
    return twist

def right_move():
    twist = Twist()
    twist.linear.x = 1

    twist.angular.z = - 1.0
    Twist_pub.publish(twist)

    return twist

def stop_move():
    twist = Twist()
    twist.linear.x = -0.5 #throotle value 310 

    twist.angular.z = 0.02  # steering tegak
    Twist_pub.publish(twist)
    return twist

def no_entry_move():
    twist = Twist()
    twist.linear.x = -0.5 #throotle value 310 

    twist.angular.z = 0
    Twist_pub.publish(twist)

    return twist

def dead_end_move():
    twist = Twist()
    twist.linear.x = -0.5 #throotle value 310 

    twist.angular.z = 0
    Twist_pub.publish(twist)

    return twist

def forward_move():
    twist = Twist()
    twist.linear.x = 0

    twist.angular.z = 0
    Twist_pub.publish(twist)

    return twist

if __name__ == "__main__":
    rospy.init_node('MoveClient')
#    rospy.spin
    stop_move()
    left_move()
    rospy.sleep(2)
    stop_move()
    right_move()
    rospy.sleep(2)
    stop_move()
    forward_move()
    rospy.sleep(2)
    stop_move()


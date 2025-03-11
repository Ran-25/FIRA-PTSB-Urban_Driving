#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def publish_cmd_vel():
    # Initialize ROS node
    rospy.init_node('cmd_vel_publisher', anonymous=True)
    rospy.loginfo('cmd_vel_publisher')
    
    # Create a publisher for the cmd_vel topic
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    # Create a Twist message
    cmd_vel = Twist()
    cmd_vel.linear.x = 0.1  # Set linear velocity along x-axis
    cmd_vel.angular.z = 0.5  # Set angular velocity around z-axis
    
    # Publish the Twist message repeatedly
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        pub.publish(cmd_vel)
        rospy.loginfo('publish cmd_vel')
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_cmd_vel()
    except rospy.ROSInterruptException:
        pass

!#/usr/bin/env python3
import rospy
from rospy import loginfo
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8

twist_pub = rospy.Publisher('/cmd_vel', Twist , queue_size=1)

def follow_move(data):
    degree_val = data.data

    if degree_val == 5 and -5:
        loginfo('steering in normal position')
        twist = Twist()
        twist.linear.x = 0

        twist.angular.z = 0.02
        twist_pub.publish(twist)
    
    elif degree_val >= 10: #positif kamera ke kiri adjust steering ke kanan
        loginfo('steering in normal position')
        twist = Twist()
        twist.linear.x = 0

        twist.angular.z = - 0.3
        twist_pub.publish(twist)
    
    elif degree_val <= -10:
        loginfo('steering in normal position')
        twist = Twist()
        twist.linear.x = 0

        twist.angular.z = 0.3
        twist_pub.publish(twist)
    
    elif degree_val >= 15:
        loginfo('steering in normal position')
        twist = Twist()
        twist.linear.x = 0

        twist.angular.z = - 0.8
        twist_pub.publish(twist)
        return twist
    
    elif degree_val <= - 15:
        loginfo('steering in normal position')
        twist = Twist()
        twist.linear.x = 0

        twist.angular.z = 0.8
        twist_pub.publish(twist)
    
    elif degree_val >= 20:
        loginfo('steering in normal position')
        twist = Twist()
        twist.linear.x = 0

        twist.angular.z = -1.5
        twist_pub.publish(twist)
    
    elif degree_val <= - 20:
        loginfo('steering in normal position')
        twist = Twist()
        twist.linear.x = 0

        twist.angular.z = 1.5
        twist_pub.publish(twist)


    return twist



if __name__ == "__main__":
    rospy.init_node('followLine')
    degree_sub = rospy.Subscriber('/degree_vel', Int8, follow_move)
    follow_move(15)
#    rospy.spin

#!/usr/bin/env python3
import rospy
from rospy import loginfo
# import time
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8, String

class TwistDk():
    def __init__(self):
        rospy.loginfo("Dah masukkkk!!!")
        self.degree_sub = rospy.Subscriber('/degree_vel', Int8, self.DegreeMove)
        self.detect_sub = rospy.Subscriber('/detect_vel', String, self.detect)
        self.Twist_pub = rospy.Publisher('/cmd_velDK', Twist, queue_size=1)

    def detect(self, data):
        signboard = data.data
        
        if signboard == 'stop':
            print("stop lahh")
            twist = Twist()
            twist.linear.x = -0.5 #throotle value 310 
            twist.linear.y = 0
            twist.linear.z = 0

            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0.02  # steering tegak

            self.Twist_pub.publish(twist)

        if signboard == 'no entry':
            print("no entry lahh")
            twist = Twist()
            twist.linear.x = -0.5 #throotle value 310 
            twist.linear.z = 0

            twist.angular.x = 0
            twist.angular.z = 0
            self.Twist_pub.publish(twist)

        if signboard == 'dead end':
            print("dead end lahh")
            twist = Twist()
            twist.linear.x = -0.5 #throotle value 310 
            twist.linear.z = 0

            twist.angular.x = 0
            twist.angular.z = 2.0
            self.Twist_pub.publish(twist)

        if signboard == 'left':
            twist = Twist()
            twist.linear.x = -0.2
            twist.linear.z = 0

            twist.angular.x = 0
            twist.angular.z = 2.0
            self.Twist_pub.publish(twist)

        if signboard == 'right':
            twist = Twist()
            twist.linear.x = 1
            twist.linear.z = 0

            twist.angular.x = 0
            twist.angular.z = - 2.0
            self.Twist_pub.publish(twist)

        if signboard == 'forward':
            loginfo('depan')
            twist = Twist()
            twist.linear.x = 1
            twist.linear.z = 0

            twist.angular.x = 0
            twist.angular.z = 0
            self.Twist_pub.publish(twist)


    def DegreeMove(self, data):
        degree = data.data
        if degree is not None:
            if degree > - 10:  #dalam range 10 hingga -10
                twist = Twist()
                twist.linear.x = 0
                twist.linear.z = 0

                twist.angular.x = 0
                twist.angular.z = 0.5

                self.Twist_pub.publish(twist)

            elif degree >= 10:
                twist = Twist()
                twist.linear.x = 0
                twist.linear.z = 0

                twist.angular.x = 0
                twist.angular.z = - 0.5

                self.Twist_pub.publish(twist)

            elif degree >= 20:
                twist = Twist()
                twist.linear.x = 0
                twist.linear.z = 0

                twist.angular.x = 0
                twist.angular.z = - 1.0

                self.Twist_pub.publish(twist)

            elif degree <= - 20:
                twist = Twist()
                twist.linear.x = 0
                twist.linear.z = 0

                twist.angular.x = 0
                twist.angular.z = 1.0

                self.Twist_pub.publish(twist)

            elif degree <=  30:
                twist = Twist()
                twist.linear.x = 0
                twist.linear.z = 0

                twist.angular.x = 0
                twist.angular.z = - 1.5

                self.Twist_pub.publish(twist)

            elif degree <=  - 30:
                twist = Twist()
                twist.linear.x = 0
                twist.linear.z = 0

                twist.angular.x = 0
                twist.angular.z = 1.5

                self.Twist_pub.publish(twist)



if __name__ == "__main__":
    rospy.init_node('TwistDk')
    control = TwistDk()
    rospy.spin()

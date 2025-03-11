#!/usr/bin/env python3
import rospy
from rospy import loginfo
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8, String
from std_srvs.srv import Empty, EmptyResponse

from donkey_service.srv import *

sign = {
    'stop': [-0.5, 0],
    'no entry': [-0.5, 0],
    'dead end': [-0.5, 2.0],
    'left': [-0.2, 2.0],   
    'right': [1.0, 2.0],
    'forward': [1.0, 0],                      
}
data = None
NAME = 'twistdk_service_server'

class TwistDk():
    def __init__(self):
        rospy.init_node(NAME)
        self.twist = Twist()
        self.signboard = 'None'
        self.detect_sub = None
        self.line_detected = False
        rospy.loginfo("Service Server TwistDk")

        self.my_service = rospy.Service('twistdk_service', DistanceData, self.get_callback)
        
#        self.detected_signboard = rospy.Subscriber('/detect_signboard', String, self.get_signboard)
        self.Twist_pub = rospy.Publisher('/cmd_velDK', Twist, queue_size=1)

    def get_signboard(self, data):
        self.signboard = data.data
        if self.signboard == '':
            self.signboard = 'None' #False tp data dr sub bentuk Str
            self.line_detected = True
        
    def get_callback(self, req):
        rospy.loginfo("Service Server detection")
        loginfo("get_callback()")
        print(req)
#        print(type(request.datarequest))
#        print(dir(request.datarequest))
#        print(request.datarequest)

#            self.degree_sub = rospy.Subscriber('/degree_vel', Int8, self.DegreeMove)
#        self.detect_sub = rospy.Subscriber('/detect_signboard', String, self.detect)

        '''
        elif self.signboard != 'None':
            loginfo('runnn')
            self.detect_sub = rospy.Subscriber('/detect_signboard', String, self.detect)

        # # jika tidak nampak line, robot nampak sign
        # if not self.line_detected:
        #     self.detect_sub = rospy.Subscriber('/detect_signboard', String, self.detect)
        return EmptyResponse()
        '''
#        return EmptyResponse()
        return

    def detect(self, data):
        #self.signboard = data.data
        #detect_signboard = True
        
        if self.signboard == 'stop':
            self.twist.linear.x, self.twist.linear.y = sign['stop'][0], sign['stop'][1]
            self.Twist_pub.publish(self.twist)

        if self.signboard == 'no entry':
            self.twist.linear.x, self.twist.linear.y = sign['no entry'][0], sign['no entry'][1]
            self.Twist_pub.publish(self.twist)

        if self.signboard == 'dead end':
            self.twist.linear.x, self.twist.linear.y = sign['dead end'][0], sign['dead end'][1]
            self.Twist_pub.publish(self.twist)

        if self.signboard == 'stop':
            self.twist.linear.x, self.twist.linear.y = sign['left'][0], sign['left'][1]
            self.Twist_pub.publish(self.twist)

        if self.signboard == 'right':
            self.twist.linear.x, self.twist.linear.y = sign['right'][0], sign['right'][1]
            self.Twist_pub.publish(self.twist)

        if self.signboard == 'forward':
            self.twist.linear.x, self.twist.linear.y = sign['forward'][0], sign['forward'][1]
            self.Twist_pub.publish(self.twist)

        # if signboard == sign['stop']:
        #     self.twist.linear.x, self.twist.twist.linear.y = sign['stop'][0], sign['stop'][1]
        #     self.Twist_pub.publish(self.twist)

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
    # from donkey_service.srv import AddTwoInts,AddTwoIntsResponse
    
    try:
        control = TwistDk()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Service server shutdown")

        

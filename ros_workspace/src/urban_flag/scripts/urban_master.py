#!/usr/bin/env python3
import rospy
from rospy import loginfo
from std_msgs.msg import Bool,Int8
# from lib.line_movement_lib import follow_move
from lib.yolo_movement_lib import detect, stop_initial
from geometry_msgs.msg import Twist



class Run():
    def __init__(self):
        self.id = 7
        self.degree_val = 0
        self.bool_value = False
        self.detect_pub = rospy.Subscriber('/detect_signboard', Int8, detect)

        self.detect_sub = rospy.Subscriber('/detect', Int8, self.get_detect)
        self.degree_sub = rospy.Subscriber('/degree_vel', Int8, self.degree)
        self.detect_bool_sub  = rospy.Subscriber('/detect_bool', Bool, self.flag)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.cmd_vel = Twist()
        #self.rate = rospy.Rate(10)
        rospy.loginfo('class GetValue():')

        stop_initial()
        # rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            self.run()
            # self.rate.sleep()
        
    def get_detect(self,data):
        self.id = data.data

    def degree(self, data):
        # self.degree_vel = data.data
        if isinstance(data.data, type(None)):
            self.degree_val = 0
        self.degree_val = data.data
        print(self.degree_val)

    def flag(self, data):
        self.bool_value = data.data

    def run(self):
        conn = self.cmd_vel_pub.get_num_connections()
        while conn > 0:
            if self.bool_value:
                
                # self.bool_value = detect(self.id)
                if self.id == 0:

                    self.cmd_vel.linear.x = -0.2
                    self.cmd_vel.linear.z = 0

                    self.cmd_vel.angular.x = 0
                    self.cmd_vel.angular.z = 2.0
                    self.cmd_vel_pub.publish(self.cmd_vel)
            
                    self.bool_value == False

                if self.id == 3:
                    print("no entry lahh")
                    self.cmd_vel.linear.x = -0.5 #throotle value 310 
                    self.cmd_vel.linear.z = 0

                    self.cmd_vel.angular.x = 0
                    self.cmd_vel.angular.z = 0
                    self.cmd_vel_pub.publish(self.cmd_vel)
            
                    self.bool_value == False

                if self.id == 4:
                    print("dead end lahh")
                    self.twist.linear.x = -0.5 #throotle value 310 
                    self.twist.linear.z = 0

                    self.twist.angular.x = 0
                    self.twist.angular.z = 2.0
                    self.cmd_vel_pub.publish(self.cmd_vel)
            
                    self.bool_value == False

                if self.id == 0:
                    self.twist = Twist()
                    self.twist.linear.x = -0.2
                    self.twist.linear.z = 0

                    self.twist.angular.x = 0
                    self.twist.angular.z = 2.0
                    self.cmd_vel_pub.publish(self.cmd_vel)
            
                    self.bool_value == False

                if self.id == 2:
                    self.twist = Twist()
                    self.twist.linear.x = 1
                    self.twist.linear.z = 0

                    self.twist.angular.x = 0
                    self.twist.angular.z = - 2.0
                    self.cmd_vel_pub.publish(self.cmd_vel)
            
                    self.bool_value == False

                if self.id == 5:
                    loginfo('depan')
                    self.twist = Twist()
                    self.twist.linear.x = -0.5
                    self.twist.linear.z = 0

                    self.twist.angular.x = 0
                    self.twist.angular.z = 0

                    rospy.sleep(2)

                    self.twist.linear.x = -0.2
                    self.twist.linear.z = 0

                    self.twist.angular.x = 0
                    self.cmd_vel_pub.publish(self.cmd_vel)
            
                    self.bool_value == False
                print("buat detection command")
            # break
                    # self.rate.sleep()

            if not self.bool_value:
            # else:

                # stop_initial()
                print("follow line")

    #            print(type(self.degree_val))
                if self.degree_val <= 5 or self.degree_val >= -5:

                    loginfo('steering in normal position')

                    self.cmd_vel.linear.x = 0.2

                    self.cmd_vel.angular.z = 0.0
                    self.cmd_vel_pub.publish(self.cmd_vel)

                    #positif kamera ke kiri adjust steering ke kanan
                elif self.degree_val >= 10:
    #                print(type(self.degree_val))
                    loginfo('steering in normal position')
                    self.cmd_vel.linear.x = 0.3

                    self.cmd_vel.angular.z = - 0.3
                    self.cmd_vel_pub.publish(self.cmd_vel)

                elif self.degree_val <= -10:
                    loginfo('steering in normal position')
                    self.cmd_vel.linear.x = 0.3

                    self.cmd_vel.angular.z = 0.5
                    self.cmd_vel_pub.publish(self.cmd_vel)

                elif self.degree_val >= 15:
                    loginfo('steering in normal position')

                    self.cmd_vel.linear.x = 0.3

                    self.cmd_vel.angular.z = - 0.5
                    self.cmd_vel_pub.publish(self.cmd_vel)


                elif self.degree_val <= - 15:
                    loginfo('steering in normal position')
                    self.cmd_vel.linear.x = 0.3

                    self.cmd_vel.angular.z = 0.8
                    self.cmd_vel_pub.publish(self.cmd_vel)

                elif self.degree_val >= 20:
                    loginfo('steering in normal position')
                    self.cmd_vel.linear.x = 0.3

                    self.cmd_vel.angular.z = -1.5
                    self.cmd_vel_pub.publish(self.cmd_vel)

                elif self.degree_val <= - 20:
                    loginfo('steering in normal position')
                    self.cmd_vel.linear.x = 0.3

                    self.cmd_vel.angular.z = 1.5
                    self.cmd_vel_pub.publish(self.cmd_vel)
                else:
                    self.bool_value == True
            # break
                    # self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('master_node')    
    r = Run()
    # r.run()
    rospy.spin()


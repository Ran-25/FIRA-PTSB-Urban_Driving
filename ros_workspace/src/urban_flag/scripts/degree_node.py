#!/usr/bin/env python3
import math
import rospy
import cv2
import numpy as np
from std_msgs.msg import Empty, Int8
from sensor_msgs.msg import CompressedImage

# Drive on the LEFT side
# lineCY = 220
# lineCX = 320

# Drive on the RIGHT side
lineCY = 550 #360
lineCX = 400

class DonkeyCar(object):

    def __init__(self):
        self.ctrl_c = False
        self.cv_image = None
        self.center = None
        self.degree = None
        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.camera_callback)
        self.degree_pub = rospy.Publisher('/degree_vel', Int8, queue_size=10)

    def show_center(self, get):
        index = np.asarray(get[0])
        if index.size > 0:
            index_left = index[0]
#            print(f"value index_left: {index_left}")
            index_right = index[-1]
#            print(f"value index_right: {index_right}")
            # SHOW CENTER <--- ADJUST SINI
#            self.center = int(((index_right - index_left) / 2) + index_left)
            self.center = int(((index_left - index_right) / 2) + index_left)
            cv2.line(self.cv_image, (self.center, lineCY), (self.center, lineCY - 20), (0, 0, 255), 2)

    def draw_text(self):
        if self.center is not None:
            val_from_line = (self.center - lineCX)
            cv2.putText(
                    self.cv_image, str(val_from_line),
                    (self.center - 20, lineCY - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255), 1, cv2.LINE_AA)
            cv2.putText(
                    self.cv_image, str(self.degree),
                    (420, 600), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(
                    self.cv_image, str(lineCY),
                    (450, 500), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 1, cv2.LINE_AA)

    def degree_angle(self):
        if self.center is not None:
            # Angle line (blue)
            cv2.line(self.cv_image, (400, 720), (self.center, lineCY), (255, 0, 0), 2)
            # Imaginary Line (grey)
            cv2.line(self.cv_image, (400, lineCY), (self.center, lineCY), (0, 0, 225), 2)
            adjacent = lineCY
            opposite = self.center - lineCX
            theta = int(math.degrees(math.atan(opposite / adjacent)))
            self.degree = theta if theta is not None else 0

            self.degree_pub.publish(theta)

    def camera_callback(self, data):
        np_arr = np.frombuffer(data.data, np.uint8)
        self.cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        hsv = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2HSV)
        blur = cv2.GaussianBlur(hsv, (15, 15), 0)

        low_yellow = np.array([0, 143, 126 ])#([0, 35, 0])
        high_yellow = np.array([179, 255, 255])   #([179, 255, 60])
        yellow_mask = cv2.inRange(blur, low_yellow, high_yellow)
        yellow = cv2.bitwise_and(self.cv_image, self.cv_image, mask=yellow_mask)

        edge = cv2.Canny(yellow, 75, 150)#(yellow, 75, 150)
        lines = cv2.HoughLinesP(edge, 1, np.pi/180, 50, maxLineGap=50)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(self.cv_image, (x1, y1), (x2, y2), (255, 255, 0), 3)

        pix = np.asarray(edge)
        get = np.where(pix[lineCY - 1] == 255)
        self.show_center(get)
        self.draw_text()
        self.degree_angle()

        # draw vertical line (green)
        cv2.line(self.cv_image, (400, 0), (400, 720), (0, 255, 0), 1)
        cv2.imshow("Original", self.cv_image)
        cv2.imshow("Canny", edge)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            rospy.signal_shutdown('quit')
            cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('no_servo_node')
    donkey_car = DonkeyCar()
    rospy.spin()

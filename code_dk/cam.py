import rospy
import cv2
import numpy as np
from std_msgs.msg import Empty
from sensor_msgs.msg import CompressedImage

class DonkeyCar(object):

    def __init__(self):
        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.camera_callback)
        self.ctrl_c = False

    def camera_callback(self, data):
        np_arr = np.frombuffer(data.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        low_yellow = np.array([0, 35, 0])
        up_yellow = np.array([179, 255, 60])
        mask = cv2.inRange(hsv, low_yellow, up_yellow)
        edges = cv2.Canny(mask, 75, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
        if lines is not None:
         for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(cv_image, (x1, y1,), (x2, y2), (0, 255, 0), 5)

        center = (cv_image.shape[1] // 2, cv_image.shape[0] // 2)
        cv2.circle(cv_image, center, 5, (0, 0, 255), -1)

        if lines is not None:
            for x1, y1, x2, y2 in lines[:, 0]:
                # Calculate distance from the red dot to each line
                dist = abs((x1 + x2) / 2 - center[0])
                #if dist <= tolerance: # Adjust tolerance as needed

                        #pass
        print(dist)
        cv2.imshow("Original", center)
        cv2.imshow("Original", cv_image)
        cv2.imshow("mask", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            rospy.signal_shutdown('quit')
            cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('donkey_car_node')
    donkey_car = DonkeyCar()
    rospy.spin()

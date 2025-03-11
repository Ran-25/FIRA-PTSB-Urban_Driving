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

        center = (cv_image.shape[1] // 2, cv_image.shape[0] // 2)  # Calculate center of the image

        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        low_yellow = np.array([0, 35, 0])
        up_yellow = np.array([179, 255, 60])
        mask = cv2.inRange(hsv, low_yellow, up_yellow)
        edges = cv2.Canny(mask, 75, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)

        # Draw Hough lines and find the closest line to the red dot
        closest_line = None
        min_dist = float('inf')
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(cv_image, (x1, y1,), (x2, y2), (0, 255, 0), 5)
                # Calculate distance from the red dot to the line
                dist = abs((x1 + x2) / 2 - center[0])
                if dist < min_dist:
                    min_dist = dist
                    closest_line = line

        cv2.circle(cv_image, center, 5, (0, 0, 255), -1)

        # Draw line connecting the dot and closest Hough line
        if closest_line is not None:
            x1, y1, x2, y2 = closest_line[0]
            cv2.line(cv_image, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # Calculate distance from the dot to the closest line
        vec_line = np.array([x2 - x1, y2 - y1])
        vec_dot_to_line = np.array([x1 - center[0], y1 - center[1]])
        norm_line = np.linalg.norm(vec_line)
        if norm_line > 0:  # Avoid division by zero
            dist_to_line = np.linalg.norm(np.cross(vec_line, vec_dot_to_line)) / norm_line
        # Print the distance value on the screen
            cv2.putText(cv_image, f'Distance: {dist_to_line:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("DonkeyCar Camera", cv_image)
        cv2.imshow("Edges", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            rospy.signal_shutdown('quit')
            cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('donkey_car_node')
    donkey_car = DonkeyCar()
    rospy.spin()

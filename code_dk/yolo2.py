import rospy
import cv2
import numpy as np
from std_msgs.msg import Empty
from sensor_msgs.msg import CompressedImage
from ultralytics import YOLO

# Define the YOLO model as a global variable
model = YOLO("best11.pt")

class DonkeyCar(object):

    def __init__(self):
        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.camera_callback)
        self.ctrl_c = False

    def camera_callback(self, data):
        np_arr = np.frombuffer(data.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Perform object detection on the frame using the global model object
        result = model(cv_image)
        annotated_frame = result[0].plot()  # Annotated frame with detections
        names = model.names

        detected_labels = [
            names[int(c)] for r in result for c in r.boxes.cls
            ]
        print(detected_labels)

        if "dead end" in detected_labels:
            print("Yeaahh berjaya")

        if "stop" in detected_labels:
            print("stop lah weyy hang nak kena saman kah")



        # Display the original and annotated frames
        cv2.imshow("Original", cv_image)
        cv2.imshow("With Detections", annotated_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            rospy.signal_shutdown('quit')
            cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('donkey_car_node')
    donkey_car = DonkeyCar()
    rospy.spin()

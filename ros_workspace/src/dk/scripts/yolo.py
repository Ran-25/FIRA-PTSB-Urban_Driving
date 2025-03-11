#!/usr/bin/env python3
 # 
import rospy
import cv2
import numpy as np
from std_msgs.msg import Empty
from sensor_msgs.msg import CompressedImage
from ultralytics import YOLO

# Define the YOLO model as a global variable
model = YOLO('/home/ubuntu20/ros_workspace/src/dk/scripts/best11.pt')

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
        print(names)

        detected_labels_and_ids = [
            (names[int(c)], int(c)) for r in result for c in r.boxes.cls]

        detected_ids = [label_id[1] for label_id in detected_labels_and_ids]

        print(detected_ids)
        # detected_labels = [
        #     names[int(c)] for r in result for c in r.boxes.cls]
        # print(detected_labels)

        # if 0 in detected_labels_and_ids:
        #     print("Yeaahh berjaya")

        # if  2 in detected_labels_and_ids:
        #     print("stop lah weyy hang nak kena saman kah")

        # if any(label_id[1] == 0 for label_id in detected_labels_and_ids):
        #     print("Yeaahh berjaya")

        # if any(label_id[1] == 2 for label_id in detected_labels_and_ids):
        #  print("stop lah weyy hang nak kena saman kah")
        # Check if specific IDs are present

        if detected_ids:  # Check if the list is not empty
            id = detected_ids[0]  # Get the first (and only) element of the list
            print(id) 
            print(type(id))

            if id == 0 :
                print("Yeaahh berjaya")

            if id == 2:
                print("stop lah weyy hang nak kena saman kah")


        cv2.imshow("With Detections", annotated_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            rospy.signal_shutdown('quit')
            cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('yolo_node')
    donkey_car = DonkeyCar()
    rospy.spin()

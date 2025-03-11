#!/usr/bin/env python3
import rospy
import cv2 
import math
import numpy as np
from rospy import loginfo
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

model = YOLO('/home/ubuntu20/ros_workspace/src/dk/scripts/best11.pt')

class YoloDetect():
    def __init__(self):
        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.camera_callback)
        self.detect_pub = rospy.Publisher('/detect_vel', String, queue_size=10)
        self.pixel_per_meter = 5 # 10

    def camera_callback(self, data):
        np_arr = np.frombuffer(data.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        h, w = cv_image.shape[:2]  # Get image height and width

        center_point = (0, h)
        txt_color, txt_background, bbox_clr = ((0, 0, 0), (255, 255, 255), (255, 0, 255))
        annotator = Annotator(cv_image, line_width=2)

        # result = model(cv_image)
        results = model.track(cv_image, persist=True)
        names = model.names
        detected_labels = [names[int(c)] for r in results for c in r.boxes.cls]
        loginfo(detected_labels)

        if results[0].boxes.id is not None:
            track_ids = results[0].boxes.id.int().cpu().tolist()
            
            for box, track_id in zip(results[0].boxes.xyxy.cpu(), track_ids):
                annotator.box_label(box, label=str(track_id), color=bbox_clr)
                annotator.visioneye(box, center_point)

                x1, y1 = int((box[0] + box[2]) // 2), int((box[1] + box[3]) // 2)  # Bounding box centroid

                distance = (math.sqrt((x1 - center_point[0]) ** 2 + (y1 - center_point[1]) ** 2)) / self.pixel_per_meter

                text_size, _ = cv2.getTextSize(f"Distance: {distance:.2f} m", cv2.FONT_HERSHEY_SIMPLEX, 1.2, 3)
                cv2.rectangle(cv_image, (x1, y1 - text_size[1] - 10), (x1 + text_size[0] + 10, y1), txt_background, -1)
                cv2.putText(cv_image, f"Distance: {distance:.2f} cm", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, txt_color, 3)

                if distance >= 20:
                    if 'stop' in detected_labels:
                        # loginfo('pub lah')
                        self.detect_pub.publish('stop')

                    elif 'dead end' in detected_labels:
                        # loginfo('pub lah')
                        self.detect_pub.publish('dead end')

                    elif 'no entry' in detected_labels:
                        # loginfo('pub lah')
                        self.detect_pub.publish('no entry')

                    elif 'left' in detected_labels:
                        # loginfo('pub lah')
                        self.detect_pub.publish('left')

                    elif 'right' in detected_labels:
                        # loginfo('pub lah')
                        self.detect_pub.publish('right')

                    elif 'forward' in detected_labels:
                        # loginfo('pub lah')
                        self.detect_pub.publish('forward')


                    else:
                        print('nothing')


        cv2.imshow("yolo distance", cv_image)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            rospy.signal_shutdown('quit')
            cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('yolo_detect')
    yolo_node = YoloDetect()
    rospy.spin()

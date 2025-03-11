#!/usr/bin/env python3
import rospy
import cv2 
import math
import numpy as np
from rospy import loginfo
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
import torch
from ultralytics import YOLO

# Check if CUDA is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load YOLO model with CUDA support
model = YOLO('/home/ubuntu20/ros_workspace/src/dk/scripts/best11.pt').to(device)

class YoloDetect():
    def __init__(self):
        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.camera_callback)
        self.detect_pub = rospy.Publisher('/detect_vel', String, queue_size=10)
        self.pixel_per_meter = 10

    def camera_callback(self, data):
        np_arr = np.frombuffer(data.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        h, w = cv_image.shape[:2]  # Get image height and width

        resized_image = cv2.resize(cv_image, (640, 640))

        center_point = (0, h)
        # pixel_per_meter = 10
        txt_color, txt_background, bbox_clr = ((0, 0, 0), (255, 255, 255), (255, 0, 255))

        # Convert image to torch tensor and move it to GPU
        # image_tensor = torch.from_numpy(cv_image).float().permute(2, 0, 1).unsqueeze(0).to(device) / 255.0
        image_tensor = torch.from_numpy(resized_image).float().permute(2, 0, 1).unsqueeze(0).to(device) / 255.0

        # Perform object detection on GPU
        results = model(image_tensor)

        names = model.names
        detected_labels = [names[int(c)] for r in results for c in r.boxes.cls]
        loginfo(detected_labels)

        if results[0].boxes.id is not None:
            track_ids = results[0].boxes.id.int().cpu().tolist()
            
            for box, track_id in zip(results[0].boxes.xyxy.cpu(), track_ids):
                x1, y1 = int((box[0] + box[2]) // 2), int((box[1] + box[3]) // 2)  # Bounding box centroid

                distance = (math.sqrt((x1 - center_point[0]) ** 2 + (y1 - center_point[1]) ** 2)) / self.pixel_per_meter

                text_size, _ = cv2.getTextSize(f"Distance: {distance:.2f} m", cv2.FONT_HERSHEY_SIMPLEX, 1.2, 3)
                cv2.rectangle(cv_image, (x1, y1 - text_size[1] - 10), (x1 + text_size[0] + 10, y1), txt_background, -1)
                cv2.putText(cv_image, f"Distance: {distance:.2f} cm", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, txt_color, 3)

                if distance <= 20:
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

        cv2.imshow("Original", cv_image)
        cv2.imshow("visioneye-distance-calculation", cv_image)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            rospy.signal_shutdown('quit')
            cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('yolo_detect')
    yolo_node = YoloDetect()
    rospy.spin()

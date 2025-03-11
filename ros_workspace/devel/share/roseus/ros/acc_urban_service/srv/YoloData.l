;; Auto-generated. Do not edit!


(when (boundp 'acc_urban_service::YoloData)
  (if (not (find-package "ACC_URBAN_SERVICE"))
    (make-package "ACC_URBAN_SERVICE"))
  (shadow 'YoloData (find-package "ACC_URBAN_SERVICE")))
(unless (find-package "ACC_URBAN_SERVICE::YOLODATA")
  (make-package "ACC_URBAN_SERVICE::YOLODATA"))
(unless (find-package "ACC_URBAN_SERVICE::YOLODATAREQUEST")
  (make-package "ACC_URBAN_SERVICE::YOLODATAREQUEST"))
(unless (find-package "ACC_URBAN_SERVICE::YOLODATARESPONSE")
  (make-package "ACC_URBAN_SERVICE::YOLODATARESPONSE"))

(in-package "ROS")





(defclass acc_urban_service::YoloDataRequest
  :super ros::object
  :slots (_dataresponse ))

(defmethod acc_urban_service::YoloDataRequest
  (:init
   (&key
    ((:dataresponse __dataresponse) 0)
    )
   (send-super :init)
   (setq _dataresponse (round __dataresponse))
   self)
  (:dataresponse
   (&optional __dataresponse)
   (if __dataresponse (setq _dataresponse __dataresponse)) _dataresponse)
  (:serialization-length
   ()
   (+
    ;; int8 _dataresponse
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _dataresponse
       (write-byte _dataresponse s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _dataresponse
     (setq _dataresponse (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _dataresponse 127) (setq _dataresponse (- _dataresponse 256)))
   ;;
   self)
  )

(defclass acc_urban_service::YoloDataResponse
  :super ros::object
  :slots (_datarequest ))

(defmethod acc_urban_service::YoloDataResponse
  (:init
   (&key
    ((:datarequest __datarequest) 0)
    )
   (send-super :init)
   (setq _datarequest (round __datarequest))
   self)
  (:datarequest
   (&optional __datarequest)
   (if __datarequest (setq _datarequest __datarequest)) _datarequest)
  (:serialization-length
   ()
   (+
    ;; int8 _datarequest
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _datarequest
       (write-byte _datarequest s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _datarequest
     (setq _datarequest (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _datarequest 127) (setq _datarequest (- _datarequest 256)))
   ;;
   self)
  )

(defclass acc_urban_service::YoloData
  :super ros::object
  :slots ())

(setf (get acc_urban_service::YoloData :md5sum-) "ca9f53be18d1fb6d1c1bfa0848d05366")
(setf (get acc_urban_service::YoloData :datatype-) "acc_urban_service/YoloData")
(setf (get acc_urban_service::YoloData :request) acc_urban_service::YoloDataRequest)
(setf (get acc_urban_service::YoloData :response) acc_urban_service::YoloDataResponse)

(defmethod acc_urban_service::YoloDataRequest
  (:response () (instance acc_urban_service::YoloDataResponse :init)))

(setf (get acc_urban_service::YoloDataRequest :md5sum-) "ca9f53be18d1fb6d1c1bfa0848d05366")
(setf (get acc_urban_service::YoloDataRequest :datatype-) "acc_urban_service/YoloDataRequest")
(setf (get acc_urban_service::YoloDataRequest :definition-)
      "int8 dataresponse
---
int8 datarequest

")

(setf (get acc_urban_service::YoloDataResponse :md5sum-) "ca9f53be18d1fb6d1c1bfa0848d05366")
(setf (get acc_urban_service::YoloDataResponse :datatype-) "acc_urban_service/YoloDataResponse")
(setf (get acc_urban_service::YoloDataResponse :definition-)
      "int8 dataresponse
---
int8 datarequest

")



(provide :acc_urban_service/YoloData "ca9f53be18d1fb6d1c1bfa0848d05366")



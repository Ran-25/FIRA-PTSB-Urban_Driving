;; Auto-generated. Do not edit!


(when (boundp 'donkey_service::DistanceData)
  (if (not (find-package "DONKEY_SERVICE"))
    (make-package "DONKEY_SERVICE"))
  (shadow 'DistanceData (find-package "DONKEY_SERVICE")))
(unless (find-package "DONKEY_SERVICE::DISTANCEDATA")
  (make-package "DONKEY_SERVICE::DISTANCEDATA"))
(unless (find-package "DONKEY_SERVICE::DISTANCEDATAREQUEST")
  (make-package "DONKEY_SERVICE::DISTANCEDATAREQUEST"))
(unless (find-package "DONKEY_SERVICE::DISTANCEDATARESPONSE")
  (make-package "DONKEY_SERVICE::DISTANCEDATARESPONSE"))

(in-package "ROS")





(defclass donkey_service::DistanceDataRequest
  :super ros::object
  :slots (_dataresponse ))

(defmethod donkey_service::DistanceDataRequest
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
    ;; byte _dataresponse
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; byte _dataresponse
       (write-byte _dataresponse s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; byte _dataresponse
     (setq _dataresponse (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _dataresponse 127) (setq _dataresponse (- _dataresponse 256)))
   ;;
   self)
  )

(defclass donkey_service::DistanceDataResponse
  :super ros::object
  :slots (_datarequest ))

(defmethod donkey_service::DistanceDataResponse
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
    ;; byte _datarequest
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; byte _datarequest
       (write-byte _datarequest s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; byte _datarequest
     (setq _datarequest (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _datarequest 127) (setq _datarequest (- _datarequest 256)))
   ;;
   self)
  )

(defclass donkey_service::DistanceData
  :super ros::object
  :slots ())

(setf (get donkey_service::DistanceData :md5sum-) "89951c538fe0bce2d7e1746ebb68223c")
(setf (get donkey_service::DistanceData :datatype-) "donkey_service/DistanceData")
(setf (get donkey_service::DistanceData :request) donkey_service::DistanceDataRequest)
(setf (get donkey_service::DistanceData :response) donkey_service::DistanceDataResponse)

(defmethod donkey_service::DistanceDataRequest
  (:response () (instance donkey_service::DistanceDataResponse :init)))

(setf (get donkey_service::DistanceDataRequest :md5sum-) "89951c538fe0bce2d7e1746ebb68223c")
(setf (get donkey_service::DistanceDataRequest :datatype-) "donkey_service/DistanceDataRequest")
(setf (get donkey_service::DistanceDataRequest :definition-)
      "# request params
byte dataresponse
---
# response params
byte datarequest

")

(setf (get donkey_service::DistanceDataResponse :md5sum-) "89951c538fe0bce2d7e1746ebb68223c")
(setf (get donkey_service::DistanceDataResponse :datatype-) "donkey_service/DistanceDataResponse")
(setf (get donkey_service::DistanceDataResponse :definition-)
      "# request params
byte dataresponse
---
# response params
byte datarequest

")



(provide :donkey_service/DistanceData "89951c538fe0bce2d7e1746ebb68223c")



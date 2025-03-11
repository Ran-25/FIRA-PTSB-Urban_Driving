; Auto-generated. Do not edit!


(cl:in-package acc_urban_service-srv)


;//! \htmlinclude YoloData-request.msg.html

(cl:defclass <YoloData-request> (roslisp-msg-protocol:ros-message)
  ((dataresponse
    :reader dataresponse
    :initarg :dataresponse
    :type cl:fixnum
    :initform 0))
)

(cl:defclass YoloData-request (<YoloData-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <YoloData-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'YoloData-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name acc_urban_service-srv:<YoloData-request> is deprecated: use acc_urban_service-srv:YoloData-request instead.")))

(cl:ensure-generic-function 'dataresponse-val :lambda-list '(m))
(cl:defmethod dataresponse-val ((m <YoloData-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader acc_urban_service-srv:dataresponse-val is deprecated.  Use acc_urban_service-srv:dataresponse instead.")
  (dataresponse m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <YoloData-request>) ostream)
  "Serializes a message object of type '<YoloData-request>"
  (cl:let* ((signed (cl:slot-value msg 'dataresponse)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <YoloData-request>) istream)
  "Deserializes a message object of type '<YoloData-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'dataresponse) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<YoloData-request>)))
  "Returns string type for a service object of type '<YoloData-request>"
  "acc_urban_service/YoloDataRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'YoloData-request)))
  "Returns string type for a service object of type 'YoloData-request"
  "acc_urban_service/YoloDataRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<YoloData-request>)))
  "Returns md5sum for a message object of type '<YoloData-request>"
  "ca9f53be18d1fb6d1c1bfa0848d05366")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'YoloData-request)))
  "Returns md5sum for a message object of type 'YoloData-request"
  "ca9f53be18d1fb6d1c1bfa0848d05366")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<YoloData-request>)))
  "Returns full string definition for message of type '<YoloData-request>"
  (cl:format cl:nil "int8 dataresponse~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'YoloData-request)))
  "Returns full string definition for message of type 'YoloData-request"
  (cl:format cl:nil "int8 dataresponse~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <YoloData-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <YoloData-request>))
  "Converts a ROS message object to a list"
  (cl:list 'YoloData-request
    (cl:cons ':dataresponse (dataresponse msg))
))
;//! \htmlinclude YoloData-response.msg.html

(cl:defclass <YoloData-response> (roslisp-msg-protocol:ros-message)
  ((datarequest
    :reader datarequest
    :initarg :datarequest
    :type cl:fixnum
    :initform 0))
)

(cl:defclass YoloData-response (<YoloData-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <YoloData-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'YoloData-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name acc_urban_service-srv:<YoloData-response> is deprecated: use acc_urban_service-srv:YoloData-response instead.")))

(cl:ensure-generic-function 'datarequest-val :lambda-list '(m))
(cl:defmethod datarequest-val ((m <YoloData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader acc_urban_service-srv:datarequest-val is deprecated.  Use acc_urban_service-srv:datarequest instead.")
  (datarequest m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <YoloData-response>) ostream)
  "Serializes a message object of type '<YoloData-response>"
  (cl:let* ((signed (cl:slot-value msg 'datarequest)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <YoloData-response>) istream)
  "Deserializes a message object of type '<YoloData-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'datarequest) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<YoloData-response>)))
  "Returns string type for a service object of type '<YoloData-response>"
  "acc_urban_service/YoloDataResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'YoloData-response)))
  "Returns string type for a service object of type 'YoloData-response"
  "acc_urban_service/YoloDataResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<YoloData-response>)))
  "Returns md5sum for a message object of type '<YoloData-response>"
  "ca9f53be18d1fb6d1c1bfa0848d05366")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'YoloData-response)))
  "Returns md5sum for a message object of type 'YoloData-response"
  "ca9f53be18d1fb6d1c1bfa0848d05366")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<YoloData-response>)))
  "Returns full string definition for message of type '<YoloData-response>"
  (cl:format cl:nil "int8 datarequest~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'YoloData-response)))
  "Returns full string definition for message of type 'YoloData-response"
  (cl:format cl:nil "int8 datarequest~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <YoloData-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <YoloData-response>))
  "Converts a ROS message object to a list"
  (cl:list 'YoloData-response
    (cl:cons ':datarequest (datarequest msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'YoloData)))
  'YoloData-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'YoloData)))
  'YoloData-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'YoloData)))
  "Returns string type for a service object of type '<YoloData>"
  "acc_urban_service/YoloData")
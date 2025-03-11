; Auto-generated. Do not edit!


(cl:in-package donkey_service-srv)


;//! \htmlinclude DistanceData-request.msg.html

(cl:defclass <DistanceData-request> (roslisp-msg-protocol:ros-message)
  ((dataresponse
    :reader dataresponse
    :initarg :dataresponse
    :type cl:integer
    :initform 0))
)

(cl:defclass DistanceData-request (<DistanceData-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DistanceData-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DistanceData-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name donkey_service-srv:<DistanceData-request> is deprecated: use donkey_service-srv:DistanceData-request instead.")))

(cl:ensure-generic-function 'dataresponse-val :lambda-list '(m))
(cl:defmethod dataresponse-val ((m <DistanceData-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader donkey_service-srv:dataresponse-val is deprecated.  Use donkey_service-srv:dataresponse instead.")
  (dataresponse m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DistanceData-request>) ostream)
  "Serializes a message object of type '<DistanceData-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dataresponse)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DistanceData-request>) istream)
  "Deserializes a message object of type '<DistanceData-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dataresponse)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DistanceData-request>)))
  "Returns string type for a service object of type '<DistanceData-request>"
  "donkey_service/DistanceDataRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DistanceData-request)))
  "Returns string type for a service object of type 'DistanceData-request"
  "donkey_service/DistanceDataRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DistanceData-request>)))
  "Returns md5sum for a message object of type '<DistanceData-request>"
  "89951c538fe0bce2d7e1746ebb68223c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DistanceData-request)))
  "Returns md5sum for a message object of type 'DistanceData-request"
  "89951c538fe0bce2d7e1746ebb68223c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DistanceData-request>)))
  "Returns full string definition for message of type '<DistanceData-request>"
  (cl:format cl:nil "# request params~%byte dataresponse~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DistanceData-request)))
  "Returns full string definition for message of type 'DistanceData-request"
  (cl:format cl:nil "# request params~%byte dataresponse~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DistanceData-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DistanceData-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DistanceData-request
    (cl:cons ':dataresponse (dataresponse msg))
))
;//! \htmlinclude DistanceData-response.msg.html

(cl:defclass <DistanceData-response> (roslisp-msg-protocol:ros-message)
  ((datarequest
    :reader datarequest
    :initarg :datarequest
    :type cl:integer
    :initform 0))
)

(cl:defclass DistanceData-response (<DistanceData-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DistanceData-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DistanceData-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name donkey_service-srv:<DistanceData-response> is deprecated: use donkey_service-srv:DistanceData-response instead.")))

(cl:ensure-generic-function 'datarequest-val :lambda-list '(m))
(cl:defmethod datarequest-val ((m <DistanceData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader donkey_service-srv:datarequest-val is deprecated.  Use donkey_service-srv:datarequest instead.")
  (datarequest m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DistanceData-response>) ostream)
  "Serializes a message object of type '<DistanceData-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'datarequest)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DistanceData-response>) istream)
  "Deserializes a message object of type '<DistanceData-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'datarequest)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DistanceData-response>)))
  "Returns string type for a service object of type '<DistanceData-response>"
  "donkey_service/DistanceDataResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DistanceData-response)))
  "Returns string type for a service object of type 'DistanceData-response"
  "donkey_service/DistanceDataResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DistanceData-response>)))
  "Returns md5sum for a message object of type '<DistanceData-response>"
  "89951c538fe0bce2d7e1746ebb68223c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DistanceData-response)))
  "Returns md5sum for a message object of type 'DistanceData-response"
  "89951c538fe0bce2d7e1746ebb68223c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DistanceData-response>)))
  "Returns full string definition for message of type '<DistanceData-response>"
  (cl:format cl:nil "# response params~%byte datarequest~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DistanceData-response)))
  "Returns full string definition for message of type 'DistanceData-response"
  (cl:format cl:nil "# response params~%byte datarequest~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DistanceData-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DistanceData-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DistanceData-response
    (cl:cons ':datarequest (datarequest msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DistanceData)))
  'DistanceData-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DistanceData)))
  'DistanceData-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DistanceData)))
  "Returns string type for a service object of type '<DistanceData>"
  "donkey_service/DistanceData")
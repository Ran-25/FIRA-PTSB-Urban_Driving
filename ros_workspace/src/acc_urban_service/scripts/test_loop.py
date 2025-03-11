#!/usr/bin/env python3
import rospy
from acc_urban_service.srv import *

def your_service_callback(req):
    # Process the request
    # For simplicity, let's assume the server always processes the request successfully
    # Prepare the response
    res = YoloDataResponse()
    res.datarequest = 99
    return res

def your_client():
    rospy.wait_for_service('twistdk_service')
    service_proxy = rospy.ServiceProxy('twistdk_service', YoloData)
    # Call the service
    d = 22
    response = service_proxy(d)
    # Process the response
    # For simplicity, let's assume the client always receives a response
    rospy.loginfo("Received response from server: %s" % response.datarequest)

if __name__ == "__main__":
    rospy.init_node('your_node')
#    rospy.Service('twistdk_service', YoloData, your_service_callback)
    
    # Continuously run both client and server
    while not rospy.is_shutdown():
        your_client()
        rospy.spin()

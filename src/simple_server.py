#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse

def serverCallback(request):
    rospy.loginfo("The service has been called")
    
    #pregenerated class for returning something
    return EmptyResponse()

def main():
    rospy.init_node("service_server")
    
    #create the service server
    my_service = rospy.Service("/my_service", Empty, serverCallback)
    
    #keep the server open
    rospy.spin()
    
if __name__=='__main__':
    main()
#!/usr/bin/env python
#0
import rospy
import socket
import sys

def Python_version():      
    socket.gethostname()
    rospy.init_node('Python_version', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
    	rospy.loginfo(sys.version)
        rate.sleep()    	   

if __name__ == '__main__':
    try:
        Python_version()
    except rospy.ROSInterruptException:
        pass
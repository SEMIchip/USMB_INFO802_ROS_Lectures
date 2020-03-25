#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys

def move_turtlebot():

    rospy.init_node('move_turtlebot', anonymous=False)
    pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)  
    rate = rospy.Rate(1) # 1hz
    vel = Twist()
    
    while not rospy.is_shutdown():
        vel.linear.x = lin_vel
        vel.angular.z = ang_vel
        pub.publish(vel)    
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtlebot(float(sys.argv[1]),float(sys.argv[2]))
    except rospy.ROSInterruptException:
        pass

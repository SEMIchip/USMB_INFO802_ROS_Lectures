#! /usr/bin/env python3

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
    move_turtlebot(float(sys.argv[1]),float(sys.argv[2]))

#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys


#/turtle1/Pose topic callback
def pose_callback(XXXXX):
    XXXXXXXXXX #printout in the console the pose of turtle1


def move_turtle(lin_vel,ang_vel):
    rospy.init_node('move_turtle', anonymous=False)

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    #Creating new subscriber: Topic name= /turtle1/pose: Callback name: pose_callback
    XXXXXXXXXXXXXXXXXXX

    rate = rospy.Rate(10) # 10hz
 
    vel = Twist()  
    while not rospy.is_shutdown():
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel

        rospy.loginfo("Linear Vel = %f: Angular Vel =%f",lin_vel,ang_vel)

        pub.publish(vel)
    
        rate.sleep()


if __name__ == '__main__':
    try:
    #Providing linear and angular velocity through command line
        move_turtle(float(sys.argv[1]),float(sys.argv[2]))
    except rospy.ROSInterruptException:
        pass

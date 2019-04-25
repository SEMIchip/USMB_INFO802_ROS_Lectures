#! /usr/bin/python

import rospy
from geometry_msgs.msg import Twist

def move_turtle():

     # Create a publisher to "talk" to Turtlesim 
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
     
    # Create a Twist message and add linear x and angular z values
    vel = Twist()
    vel.linear.x = 1.0

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(10)

    # For the next 6 seconds publish vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(6):
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python

import rospy
XXXXXXXXXXXX   # import Twist

def move_turtle():

    # Initialize node
    XXXXXXXXXXXX
   
    # Create a publisher to "talk" to Turtlesim 
    pub = XXXXXXXXXXXX
     
    # Create a Twist message and change linear x value
    vel = Twist()
    vel.linear.x = 1.0  # Move along the x axis only

    # Save current time and set publish rate at 10 Hz
    tStart = rospy.Time.now()
    rate = rospy.Rate(10)

    # For the next 6 seconds publish vel move commands to Turtlesim
    while rospy.Time.now() < tStart + rospy.Duration.from_sec(6):
        XXXXXXXXXXXX  # publish velocity command to the Turtlesim
        rate.sleep()

          
if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass

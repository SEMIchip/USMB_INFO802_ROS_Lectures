#!/usr/bin/env python

import rospy   # Import rospy library
XXXXXXXXXXXX   # Import Twist message

def move_turtle():

    # Initialize node
    XXXXXXXXXXXX
   
    # Create a publisher to "talk" to Turtlesim 
    pub = XXXXXXXXXXXX
     
    # Create a Twist message and change linear x value
    vel = Twist()       # Creates a 'Twist object'
    vel.linear.x = 1.0  # Changing the 'x' value in the 'linear' vector of the 'Twist' object. (Move along the x axis only)

    # Save current time and set publish rate at 10 Hz
    tStart = rospy.Time.now()
    rate = rospy.Rate(10)

    # For the next 6 seconds publish vel move commands to Turtlesim
    while rospy.Time.now() < tStart + rospy.Duration.from_sec(6):
        XXXXXXXXXXXX  # Publishes velocity command to the Turtlesim
        rate.sleep()

          
if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
#!/usr/bin/env python
# -*- coding utf-8 -*-

import rospy
rospy.init_node('hello_python')

rate = rospy.Rate(10)

while not rospy.is_shutdown():
  print "hello ROS python"
  rate.sleep()

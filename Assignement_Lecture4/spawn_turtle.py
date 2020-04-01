#!/usr/bin/env python

import rospy
from turtlesim.srv import Spawn
import random

x = random.uniform(0,10)
y = random.uniform(0,10)

rospy.wait_for_service('spawn')
spawner = rospy.ServiceProxy('spawn', Spawn)
spawner(x, y, 0.5, 'turtle2')

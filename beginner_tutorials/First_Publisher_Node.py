#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def First_Publisher_Node():
    pub = rospy.Publisher('numbers', Int32, queue_size=10)
    
    rospy.init_node('First_Publisher_Node', anonymous=True)

    rate = rospy.Rate(10)

    number_count=0
    while not rospy.is_shutdown():
        rospy.loginfo(number_count)
        pub.publish(number_count)
        rate.sleep()
        number_count +=1

if __name__ == '__main__':
    try:
        First_Publisher_Node()
    except rospy.ROSInterruptException:
        pass


#!/usr/bin/python
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
  
  
def First_Subscriber_Node():

    rospy.init_node('First_Subscriber_Node', anonymous=True)

    rospy.Subscriber('numbers', Int32, callback)

    rospy.spin()


if __name__ == '__main__':
    try:
        First_Subscriber_Node()
    except rospy.ROSInterruptException:
        pass


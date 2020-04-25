#!/usr/bin/python
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data.data) # Displays IN THE CONSOLE, the message read on the topic
  
def First_Subscriber_Node():

    rospy.init_node('First_Subscriber_Node', anonymous=True)

    rospy.Subscriber('numbers', Int32, callback) # Substribes to topic "/numbers" and a read message of type Int32

    rospy.spin()


if __name__ == '__main__':
    try:
        First_Subscriber_Node()
    except rospy.ROSInterruptException:
        pass

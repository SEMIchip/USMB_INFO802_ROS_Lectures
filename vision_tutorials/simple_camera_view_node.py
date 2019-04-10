#! /usr/bin/python

import rospy                                  # rospy for the subscriber
from sensor_msgs.msg import Image             # ROS Image message
from cv_bridge import CvBridge                # ROS Image message -> OpenCV2 image converter
import cv2                                    # OpenCV2 for saving an image


bridge = CvBridge()                           # Instantiate CvBridge object


def image_callback(msg):
    cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")   # Convert your ROS Image message to OpenCV2
    cv2.imshow("Usb camera video", cv2_img)
    cv2.waitKey(3)


def simple_camera_display():
    rospy.init_node('image_subscriber')
    image_topic = "/usb_cam/image_raw"                     # Define your image topic

    rospy.Subscriber(image_topic, Image, image_callback)   # Set up your subscriber and define its callback
    rospy.spin()                                           # Spin until ctrl + c



if __name__ == '__main__':
    simple_camera_display()

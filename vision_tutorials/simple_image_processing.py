#! /usr/bin/python

import rospy                                  # rospy for the subscriber
from sensor_msgs.msg import Image             # ROS Image message
from cv_bridge import CvBridge                # ROS Image message -> OpenCV2 image converter
import cv2                                    # OpenCV2 for saving an image
import numpy as np


bridge = CvBridge()                           # Instantiate CvBridge object


def image_callback(msg):
    cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")   # Convert your ROS Image message to OpenCV2 
    frame = np.array(cv2_img, dtype=np.uint8) # Convert the image to a Numpy array since most cv2 functions. Require Numpy arrays.
    color_image = color_detection(frame)      # Process the frame using the circle_detection() function
    cv2.waitKey(3)


def color_detection(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)     # Converts images from BGR to HSV 

    blue_lower = np.array([90,50,50],np.uint8)       # Defining the range of Blue color
    blue_upper = np.array([120,255,255],np.uint8)

    mask = cv2.inRange(hsv, blue_lower, blue_upper)  # Finding the range blue colour in the image

    cv2.imshow("image mask",mask)

    # The bitwise and of the frame and mask is done so that only the blue coloured objects are highlighted  
    # and stored in res 
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow("color",res)
  
    return res


def simple_image_processing():
    rospy.init_node('image_subscriber')
    image_topic = "/usb_cam/image_raw"                     # Define your image topic

    rospy.Subscriber(image_topic, Image, image_callback)   # Set up your subscriber and define its callback
    rospy.spin()                                           # Spin until ctrl + c



if __name__ == '__main__':
    simple_image_processing()

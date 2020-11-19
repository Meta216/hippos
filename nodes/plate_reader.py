#!/usr/bin/env python2

"""
Subscribe to license plate image topics and itentify them with a neural network.
"""

import time

import rospy
import sensor_msgs
import std_msgs
import cv_bridge

import util

bridge = cv_bridge.CvBridge()


def id_plate(frame):
    return None


def read_plate(frame):
    return "AA12"


def process_frame(ros_image, score):
    frame = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    location = id_plate(frame)
    if location is not None:
        reading = read_plate(frame)
        score.publish(util.plate_message(location, reading))


if __name__ == "__main__":
    rospy.init_node("plate_reader", anonymous=True)
    score = rospy.Publisher(util.topics.plates, std_msgs.msg.String, queue_size=1)
    rospy.Subscriber(
        util.topics.camera, sensor_msgs.msg.Image, process_frame, callback_args=score
    )

    time.sleep(1)

    rospy.spin()

#! /usr/bin/env python

import rospy
import pickle
import os
import tf2_ros

if __name__ == '__main__':

    rospy.init_node('tf_saver')
    rospy.loginfo("TF saver started!")

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    rospy.sleep(1)
    stored_data = {}

    ##### FILL IN THE APPROPRIATE FILENAME. HINT: USE `raw_input()`
    file_name = raw_input("Vnesi ime datoteke za shranjevanje: ")
    outfile = open(file_name,'wb')
    saved_data = {}
    #########################
    ##### STUDENT WRITES ####
    #########################

    saved_frames=["world","frame_1","frame_2"]
    # Hint - Use the tf_buffer.lookup_transform() method to retrieve the transform.
    # Example:
    transformation = tf_buffer.lookup_transform(saved_frames[0], saved_frames[1], rospy.Time(0))
    saved_data[raw_input("Ime transformacije: ")] = transformation

    transformation = tf_buffer.lookup_transform(saved_frames[1], saved_frames[2], rospy.Time(0))
    saved_data[raw_input("Ime transformacije: ")] = transformation

    transformation = tf_buffer.lookup_transform(saved_frames[0], saved_frames[2], rospy.Time(0))
    saved_data[raw_input("Ime transformacije: ")] = transformation
    # Note - from_frame and to_frame need to be defined!


    #########################

    pickle.dump(saved_data, outfile)
    outfile.close()
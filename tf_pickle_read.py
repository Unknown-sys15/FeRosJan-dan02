#! /usr/bin/env python

import rospy
import pickle
import tf2_ros
from geometry_msgs.msg import TransformStamped

if __name__ == '__main__':

    # Init the node
    rospy.init_node('tf_loader')
    tf_broad = tf2_ros.StaticTransformBroadcaster()


    ##### FILL IN THE APPROPRIATE FILENAME. HINT: USE `raw_input()`
    file_name = "test3"

    infile = open(file_name,'rb')
    stored_poses = pickle.load(infile)
    infile.close()
    array = []
    #print(stored_poses)
    #print(stored_poses["tf01"])
    for key in stored_poses:
        #key so tf01...
        array.append(stored_poses[key])
        print(key)

    print(array)
    tf_broad.sendTransform(array)
    #########################
    ##### STUDENT WRITES ####
    #########################


    #########################
    rospy.spin()

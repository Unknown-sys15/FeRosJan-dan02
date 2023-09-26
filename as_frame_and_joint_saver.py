from sensor_msgs.msg import JointState
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

    name = "  "
    while not rospy.is_shutdown():
        name = raw_input("Transformation name(exit to quit): ")
        if (name == 'exit'):
            break
        transformation = tf_buffer.lookup_transform("base_link", "tool0", rospy.Time(0))
        transformation.child_frame_id = name
        joints = rospy.wait_for_message('/joint_states', JointState, rospy.Duration(1))
        print(transformation)
        print(joints)
        print("###############################################################")
        saved_data[name] = [transformation,joints]
        
    
    pickle.dump(saved_data, outfile)
    outfile.close()


    #transformation = tf_buffer.lookup_transform(saved_frames[0], saved_frames[2], rospy.Time(0))
    #saved_data[raw_input("Ime transformacije: ")] = transformation
    # Note - from_frame and to_frame need to be defined!


    #########################

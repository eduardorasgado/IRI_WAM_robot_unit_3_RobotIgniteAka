#! /usr/bin/env python
import rospy
import rospkg
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest

rospy.init_node('move_iri_wam_with_service') # Initialise a ROS node

# Wait for the service client to be running
rospy.wait_for_service('/execute_trajectory') 

#init the service server
service_path = rospy.ServiceProxy('/execute_trajectory', ExecTraj) # Create the connection to the service 

#create a request object
execute_a_path = ExecTrajRequest()

#initialize a ros pkg directory handler
rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

try:
    rospy.loginfo("Executing...")
    #like in msgs, we have to fill the correct file field inside the srv file in srv folder
    execute_a_path.file = traj
    
    #our filled object path insode the service
    service_path(execute_a_path)
    rospy.loginfo("SERVICE GET_FOOD PATH SUCCEEDED!")
except Exception as e:
    print("Failure to execute.")
    pass

finally:
    rospy.loginfo("Finished.")
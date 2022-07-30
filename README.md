# Four-wheeled-Robot

Create a catkin workspace and copy the my_robot package in /catkin_ws/src/   
You need to make the config.cfg file executable   
   
# Running the code:   
   
Gazebo launch:   
roslaunch my_robot gazebo.launch   
   
Inorder to run the pid controller:   
rosrun my_robot my_robot   
   
Dynamic Reconfigure:   
rosrun rqt_reconfigure rqt_reconfigure
   
Mapping:   
1) roslaunch my_robot gazebo.launch   
2) roslaunch my_robot mapping.launch -- uses gmapping package   
   
Running Navigation Stack:   
1) roslaunch my_robot gazebo.launch   
2) roslaunch my_robot localisation.launch -- uses amcl package

# UR5-With-Robotiq85 #
##Installation##

Note: Following steps are based on UBUNTU 16.04 with ROS-kinetic

This step assumes that your PC is running with Ubuntu 16 and configured with ROS KINETIC and all required libraries 

Creating Work Space and cloning UR5-With-Robotiq85 and universal_robot package

     mkdir –p ~/catkin_ws/src
     cd ~/catkin_ws/src
     git clone https://github.com/gaitech-robotics/UR5-With-Robotiq85.git
     git clone https://github.com/gaitech-robotics/universal_robot.git
     cd ~/catkin_ws && catkin_make

## Basic Usage ##
### Launch the decsciption ###
    roslaunch ur5_robotiq85_description ur5_robotiq85_upload.launch
### Bringup the robotiq85 ###
    roslaunch robotiq_85_bringup robotiq_85.launch
### Bringup the UR5 Arm ###
    roslaunch ur_morden_driver ur5_bringup.launch
### Bringup the move group ###
    roslaunch ur5_robotiq85_moveit_config move_group.launch

#### Modification Process: ####

- <font size=4> Turn off the loading of the model description in ur5_bringup launch file. </font>
- <font size=4> Turn off the startup of the ur5 arm robot\_sate\_publish node. </font>
- <font size=4> Remap the ur5 arm joint states publish topic from /joint\_states to /ur\_arm/joint\_states. </font>
- <font size=4> Turn off the startup of the robotiq85 robot\_sate\_publish node and joint\_sate\_publish node. </font>
- <font size=4> Turn off the loading of the model description in robotiq\_85\_bringup launch file. </font>
- <font size=4> In ur5\_robotiq85\_upload launch file add robot\_sate\_publish node, joint\_sate\_publish node and load the new robot description file. </font>
- <font size=4> Add /gripper/joint\_states and /ur\_arm/joint\_states into the joint\_sate\_publish node source list. </font>
- <font size=4> Base on the new description file make a new moveit congfig package. </font>



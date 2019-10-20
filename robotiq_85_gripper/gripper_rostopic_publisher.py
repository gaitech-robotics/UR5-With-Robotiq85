#! /usr/bin/env python

import rospy                              
from robotiq_85_msgs.msg import GripperCmd

rospy.init_node('gripper_motion_publisher')        
pub = rospy.Publisher('/gripper/cmd', GripperCmd)
                                           
rate = rospy.Rate(0.5)         
            
var = GripperCmd()
var.speed = 0.1
var.force = 0.1                        

while not rospy.is_shutdown():            
                         
  print"Publishing motion commands for gripper"
  
  var.position = 1.0
  pub.publish(var)
  rate.sleep()
  
  var.position = 0.06
  pub.publish(var)
  rate.sleep()
  
  var.position = 0.03
  pub.publish(var)
  rate.sleep()
  
  var.position = 0.0
  pub.publish(var)
  rate.sleep()
  
  var.position = 0.03
  pub.publish(var)
  rate.sleep()
  
  var.position = 0.06
  pub.publish(var)
  rate.sleep()

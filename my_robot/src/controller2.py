#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt

class myrobot():

    def __init__(self):
        rospy.init_node('myrobot_controller',anonymous=True)
        self.velocity_publisher=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        self.pose_subs=rospy.Subscriber('/pose',Pose,self.callback)
        self.pose=Pose()
        self.rate=rospy.Rate(10)

    def callback(self,data):
        self.pose=data
        self.pose.x=round(self.pose.x,4)
        self.pose.y=round(self.pose.y,4)

    def getdistance(self,target_x,target_y):
        distance=sqrt(pow((target_x-self.pose.x),2)+pow((target_y-self.pose.y),2))
        return distance

    def move(self):
        target_pose=Pose()
        target_pose.x=4
        target_pose.y=5
        tolerance=0.9
        vel_msg=Twist()

        while sqrt(pow((target_pose.x-self.pose.x),2)+pow((target_pose.y-self.pose.y),2))>=tolerance:

            #linear velocity
            vel_msg.linear.x=0.5*sqrt(pow((target_pose.x-self.pose.x),2)+pow((target_pose.y-self.pose.y),2))
            vel_msg.linear.y=0
            vel_msg.linear.z=0

            #angular velocity
            vel_msg.angular.x=0
            vel_msg.angular.y=0
            vel_msg.angular.z=1*(atan2(target_pose.y - self.pose.y, target_pose.x - self.pose.x) - self.pose.theta)

            #publishing our velocity
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

        #to stop bot on reaching destination
        vel_msg.linear.x=0
        vel_msg.angular.z=0
        self.velocity_publisher.publish(vel_msg)

        rospy.spin()


if __name__=='__main__':
        try:
            s=myrobot()
            s.move()
        except rospy.ROSInterruptException: pass


#plot juggler , rqt_reconfigure

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
from math import pow,atan2,sqrt

class myrobot():

    def __init__(self):
        rospy.init_node('myrobot_controller',anonymous=True)
        self.velocity_publisher=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        self.pose_subs=rospy.Subscriber('/pose2d',Pose2D,self.callback)
        self.pose=Pose2D()
        self.rate=rospy.Rate(2)

    def callback(self,data):
        self.pose=data
        self.pose.x=round(self.pose.x,4)
        self.pose.y=round(self.pose.y,4)

    def getdistance(self,target_x,target_y):
        distance=sqrt(pow((target_x-self.pose.x),2)+pow((target_y-self.pose.y),2))
        return distance

    def move(self):
        target_pose=Pose2D()
        target_pose.x=0.5
        target_pose.y=0.5
        tolerance=0.5
        vel_msg=Twist()

        while sqrt(pow((target_pose.x-self.pose.x),2)+pow((target_pose.y-self.pose.y),2))>=tolerance:

            #linear velocity
            vel_msg.linear.x=0.1*sqrt(pow((target_pose.x-self.pose.x),2)+pow((target_pose.y-self.pose.y),2))
            vel_msg.linear.y=0
            vel_msg.linear.z=0

            #angular velocity
            vel_msg.angular.x=0
            vel_msg.angular.y=0
            vel_msg.angular.z=0.001*(atan2(target_pose.y - self.pose.y, target_pose.x - self.pose.x) - self.pose.theta)

            if target_pose.x-self.pose.x ==0 and target_pose.y-self.pose.y==0:
            	break

            #publishing our velocity
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

        #to stop bot on reaching destination
        vel_msg.linear.x=0
        vel_msg.linear.y=0
        vel_msg.linear.z=0
        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=0
        self.velocity_publisher.publish(vel_msg)

        rospy.spin()


if __name__=='__main__':
        try:
            s=myrobot()
            s.move()
        except rospy.ROSInterruptException: pass


#plot juggler , rqt_reconfigure

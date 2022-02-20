#ifndef _PID_H_
#define _PID_H_
#include "ros/ros.h"
#include <tf/tf.h>
#include <tf/transform_datatypes.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/Point.h>
#include <nav_msgs/Odometry.h>
#include <geometry_msgs/Pose2D.h>
#include <math.h>
class Pidcontrol
{
    public:
    Pidcontrol(ros::NodeHandle &nh);

    void OdomCB(const nav_msgs::Odometry::ConstPtr& ptr);

    protected:
    double kp=0.05,kd=0.003,ki=0.0003,x=5,y=5,theta,integral_dist,integral_angle;
    double prev_error,prev_time,prev_theta_err;
    

    private:
    ros::Publisher pub;
    ros::Subscriber sub;
    

};
#endif
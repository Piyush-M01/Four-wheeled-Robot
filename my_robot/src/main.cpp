#include "../include/pid.hpp"
#include "pid.cpp"
#include "dynamic_reconfigure.cpp"

int main(int argc, char **argv) {
  ros::init(argc, argv, "my_robot");
  ros::NodeHandle nh;
  dynamic_reconfigure::Server<my_robot::configConfig> server;
  dynamic_reconfigure::Server<my_robot::configConfig>::CallbackType f;
  f=boost::bind(&callback, _1, _2);
  server.setCallback(f);
  Pidcontrol c(nh);
  ros::spin();
  return 0;
}

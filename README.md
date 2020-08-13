# LiDAR

Self-Driving performance of a Donkey car using an RpLiDAR along with Localization and Mapping of the Route

The Ros environment is setup on a Nvidia Jetson Nano mounted on top of a donkey car.

steps for running the codes:

1. clone the rplidar_hector_slam repository to your ROS environment

2. catkin_make #Builds the code in your workspace

3. Run the launch file 

4. Run the publisher file (built in python2/3)

5. Run the subscriber file (functions with donkey cars having I2C protocols)

changes can be made to the codes according to your requirements and usecases.

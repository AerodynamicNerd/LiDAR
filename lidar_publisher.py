#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
#from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray
import sys
drive_data=Int32MultiArray()
#pub = rospy.Publisher("drive", Int32MultiArray, queue_size=10)
def callback(data):
    
    c0 = []                                                             # Defining Empty arrays that store data from specific angles as defined below
    c1 = []
    c2 = []
    c3_1 = []
    c3_2 = []
    c3 = []
    c4 = []
    c5 = []
    drive_data.data=[]
    value=data.ranges
    speed=10                                                            # Providing speed and angle values from the servo motors of the donkey cars having I2C protocols
    angle=96

    for x in range(90,270):
        c0.append(value[x])

    c0 = min(c0)
    print (c0)

    for x in range(70,90):
        c1.append(value[x])

    c1 = min(c1)
    print (c1)

    for x in range(35,70):
        c2.append(value[x])

    c2 = min(c2)
    print (c2)

    for x in range(0,35):
        c3_1.append(value[x])

    c3_1 = min(c3_1)

    for x in range(325,360):
        c3_2.append(value[x])

    c3_2 = min(c3_2)
    c3 = min(c3_1,c3_2)
    print (c3)

    for x in range(250,325):
        c4.append(value[x])

    c4 = min(c4)
    print (c4)

    for x in range(250,270):
        c5.append(value[x])

    c5 = min(c5)
    print (c5)

    if c1 <= 0.4:                   # Defining control logics for the vehicle to take actions based on the objects detected in a 360 degree scenario.
       speed = 10
       angle = 142
       print('Take a Sharp Right')

    elif c2 <= 0.5:
       speed = 10
       angle = 122
       print('Turn Right')

    elif c3 <= 0.25:
       speed = 0
       angle = 96
       print('STOP!')

    elif c4 <= 0.5:
       speed = 10
       angle = 70
       print('Turn Left')

    elif c5 <= 0.4:
       speed = 10
       angle = 50
       print('Take a Sharp Left')

    drive_data.data=[speed,angle]
    pub = rospy.Publisher("drive", Int32MultiArray, queue_size=10)      # Defining a publisher node to publish the values
    rospy.loginfo(drive_data)
    pub.publish(drive_data)


def talker():
    rospy.init_node('talker', anonymous=True)

    rospy.Subscriber("/scan", LaserScan, callback, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
         pub = rospy.Publisher("drive", Int32MultiArray, queue_size=10)
         speed = 0
         angle = 100
         drive_data.data=[speed,angle]
         rospy.loginfo(drive_data)
         pub.publish(drive_data)

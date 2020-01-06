#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
#from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray
import sys
drive_data=Int32MultiArray()
#pub = rospy.Publisher("drive", Int32MultiArray, queue_size=10)
def callback(data):

    pub = rospy.Publisher("drive", Int32MultiArray, queue_size=10)
    c0 = []
    c1 = []
    c2 = []
    c3_1 = []
    c3_2 = []
    c3 = []
    c4 = []
    c5 = []
    drive_data.data=[]
    value=data.ranges
    speed=10
    angle=96
    #print (value)

    for x in range(60,300):
        c0.append(value[x])

    c0 = min(c0)
    print (c0)

    for x in range(45,60):
        c1.append(value[x])

    c1 = min(c1)
    print (c1)

    for x in range(15,45):
        c2.append(value[x])

    c2 = min(c2)
    print (c2)

    for x in range(0,15):
        c3_1.append(value[x])

    c3_1 = min(c3_1)

    for x in range(345,360):
        c3_2.append(value[x])

    c3_2 = min(c3_2)
    c3 = min(c3_1,c3_2)
    print (c3)

    for x in range(315,345):
        c4.append(value[x])

    c4 = min(c4)
    print (c4)

    for x in range(300,315):
        c5.append(value[x])

    c5 = min(c5)
    print (c5)

    if c3 <= 0.22:
       speed = 0
       angle = 96

    else:
       if c1 > 0.25 and c5 > 0.25 and c2 > 0.5 and c4 > 0.5:
                   speed = 18
                   angle = 96
                   print('Go Straight!')

       elif c1 <0.4 or 0.4< c2 < 0.55 and c4 > 0.5 and c5 > 0.4:
		   speed = 15
		   angle = 96 + (8/c1)+(4/c2)
                   if angle > 140: angle = 140
                   else: angle = angle
		   print('Turn Right')

       elif c5 < 0.4 or 0.4< c4 < 0.55 and c2 > 0.5 and c1 > 0.4:
		   speed = 15
		   angle = 96 - (8/c5) - (4/c4)
                   if angle < 55: angle = 55
                   else: angle = angle
		   print('Turn Left')

       elif c2 < 0.4 and c4 > 0.5 and c5 > 0.5:
		   speed = 15
		   angle = 96 + 12/(c2)
		   print('Take a Sharp Right')

       elif c4 < 0.4 and c2 > 0.5 and c1 > 0.5:
                   speed = 15
                   angle = 96 - 12/(c4)
                   print('Take a Sharp Left')

       elif c1 < 0.3 or c2 < 0.5 and not c4 > 0.5 and not c5 > 0.4:
		   speed = 0
		   angle = 96
		   print('STOP!!')

       elif c5 < 0.3 or c4 < 0.5 and not c2 > 0.5 and not c1 > 0.4:
		   speed = 0
		   angle = 96
		   print('STOP!!')

       elif c2 < 0.3 and not c4 > 0.5 and not c5 > 0.5:
		   speed = 0
		   angle = 96
		   print('STOP!!')

       elif c4 < 0.3 and not c2 > 0.5 and not c1 > 0.5:
                   speed = 0
                   angle = 96
                   print('STOP!!')


    drive_data.data=[speed,angle]
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

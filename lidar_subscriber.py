#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def callback(data):
    speed = data.data[0]
    print(speed)
    angle = data.data[1]
    print(angle)
    kit.servo[3].angle = angle
    kit.continuous_servo[0].throttle = (speed/100)
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("drive", Int32MultiArray, callback, queue_size=10)  
    rospy.spin()
if __name__ == '__main__':
    listener()
      

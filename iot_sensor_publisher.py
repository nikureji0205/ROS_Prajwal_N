#!/usr/bin/env python3
import rospy
from ros_essentials_cpp.msg import IOTSensor
import random

pub = rospy.Publisher( 'iot_sensor_topic', IOTSensor , queue_size= 10)

rospy.init_node( 'iot_sensor_publisher_node', anonymous = True)

rate = rospy.Rate(1)
i=0
while not rospy.is_shutdown():
    iot_sensor = IOTSensor()
    iot_sensor.id = 1
    iot_sensor.name = "iot_parking_01"
    iot_sensor.temperature = 24.33 + (random.random()*2)
    iot_sensor.humidity = 33.42 + (random.random()*2)
    rospy.loginfo ("I publish:")
    rospy.loginfo("iot_sensor")
    pub.publisher(iot_sensor)
    rate.sleep()
    i=i+1

    

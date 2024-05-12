#!/usr/bin/env python3
import numpy as np
import cv2

image_name = "tree_praj"

print("read an image from file ")
color_image = cv2.imread("/home/praj/catkin_ws/src/ros_basics_tutorials/src/perception_I/images/tree_praj.jpg",cv2.IMREAD_COLOR)

print("display image in native color")
cv2.imshow("original image", color_image)
cv2.moveWindow("original images",0,0)
print(color_image.shape)

height,width,channels = color_image.shape

print ("slipt the image into three channels.")
blue,green,red = cv2.split(color_image)

cv2.imshow("blue channel",blue)
cv2.moveWindow("Blue channel",0,height)

cv2.imshow("green channel" , green)
cv2.moveWindow("green channel",0,height)

cv2.imshow("red channel" , red)
cv2.moveWindow("red channel",0,height)

print("...slipt the image into Hue , Saturation , Value channel...")
hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_image = np.concatenate((h,s,v),axis=1)
cv2.imshow("Hue , Saturation Value Images",hsv_image)
cv2.imshow("HSV Image" ,hsv)

print("...convert an image to grayscale...")
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image ", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindow()


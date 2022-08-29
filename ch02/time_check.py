import os
import sys
import cv2
import time


img = cv2.imread('ch02/image/hongkong.jpg')


if img is None:
  sys.exit()
  
tm = cv2.TickMeter()  

tm.start()

edge = cv2.Canny(img,50,150)

tm.stop()

print("Elapsed Time : {}ms".format(tm.getTimeMilli()))
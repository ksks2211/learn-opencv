import numpy as np
import cv2

img = np.ones((480,640), dtype=np.uint8)

cv2.imshow('image',img)

def on_change(pos):
  global img
  level = pos*16
  level = np.clip(level, 0,255)
  img[:,:] = level  
  cv2.imshow('image',img)
  
cv2.createTrackbar('Level','image',0,16,on_change)
cv2.waitKey()

cv2.destroyAllWindows()
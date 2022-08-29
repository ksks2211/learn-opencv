import sys
import cv2
import numpy as np


img = np.ones((480,640,3), dtype=np.uint8) * 255



prev = [-1,-1]

def on_mouse(event,x,y,flags,param):  
  global prev,img
  
  if event == cv2.EVENT_LBUTTONDOWN:
    prev = [x,y]
  elif event==cv2.EVENT_MOUSEMOVE and flags&cv2.EVENT_FLAG_LBUTTON:
    cv2.line(img,prev,[x,y],(255,0,255),3,cv2.LINE_AA)
    prev = [x,y]
    cv2.imshow('image',img)                    

cv2.imshow('image',img)
cv2.setMouseCallback('image',on_mouse)
cv2.waitKey()


cv2.destroyAllWindows()
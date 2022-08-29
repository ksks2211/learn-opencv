import sys
import cv2
import os.path as path

filename = path.join(path.dirname(__file__),'image','cat.bmp')
img1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename, cv2.IMREAD_COLOR)


h, w = img1.shape[:2]

img1[:,:] = 0
img2[:,:] = (0,255,255)


if img1 is None or img2 is None:
  print("Image load Failed")
  sys.exit()
  
  
cv2.imshow('img1', img1)  
cv2.imshow('img2',img2)
cv2.waitKey()

cv2.destroyAllWindows()
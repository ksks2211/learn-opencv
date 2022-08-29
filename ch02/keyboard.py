import sys
import cv2


img = cv2.imread('ch02/image/cat.bmp',cv2.IMREAD_GRAYSCALE)


if img is None:
  sys.exit()
  
cv2.namedWindow('image')  

cv2.imshow('image',img)


while True:
  k = cv2.waitKey()
  
  
  if k == 27:
    break
  elif k == ord('i'):
    img = ~img
    cv2.imshow('image',img)

cv2.destroyAllWindows()
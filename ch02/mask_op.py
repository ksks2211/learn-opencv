import cv2
import os.path as path




def fullname(filename:str) -> str:
  return path.join(path.dirname(__file__),'image',filename)
  
  
  
src = cv2.imread(fullname('opencv-logo-white.png'),cv2.IMREAD_UNCHANGED)  

mask = src[:,:,-1]
src = src[:,:,0:3]
dst = cv2.imread(fullname('field.bmp'),cv2.IMREAD_COLOR)


cv2.imshow('src',src)
cv2.imshow('mask',mask)





h, w = mask.shape[:2]

y,x = dst.shape[:2]

y = y//2 - h//2
x = x//2 - w//2


cv2.copyTo(src, mask, dst[y:y+h,x:w+x])



cv2.imshow('dst',dst)



cv2.imwrite( fullname('field_opencv_logo.bmp'),dst)
cv2.waitKey()

cv2.destroyAllWindows()
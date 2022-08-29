import numpy as np
import cv2
import os.path as path


filename = 'HappyFish.jpg'
fullname = path.join(path.dirname(__file__),'image',filename)


img1 = cv2.imread(fullname)

img2 = img1[40:120, 30:150]
img3 = img2.copy()

cv2.circle(img2, (50,50), 20, (0,0,255),2 )




cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)


cv2.waitKey()

cv2.destroyAllWindows()
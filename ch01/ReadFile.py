import cv2
import sys
from pathlib import Path
import os

filename = 'cat.bmp'
dirname = os.path.dirname(__file__) or '.'
fullname = os.path.join(dirname,filename)

img = cv2.imread(fullname,cv2.IMREAD_GRAYSCALE)

print(type(img))

if img is None:
  print("Image load Failed!!!")
  sys.exit()
  
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)  
cv2.imshow('image',img)
cv2.waitKey()


save_name = os.path.join(dirname,'cat2.png')


cv2.imwrite(save_name, img, [cv2.IMWRITE_JPEG_QUALITY,90])


cv2.destroyAllWindows()
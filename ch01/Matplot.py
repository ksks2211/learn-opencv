import matplotlib.pyplot as plt
import cv2
import os.path as path





filename = "cat.bmp"
fullname = path.join(path.dirname(__file__),filename)

imgBGR = cv2.imread(fullname)
imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)
imgGray = cv2.imread(fullname,cv2.IMREAD_GRAYSCALE)



plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray,cmap='gray')

plt.show()
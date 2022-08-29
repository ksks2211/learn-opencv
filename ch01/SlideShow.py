import sys
import glob
import os.path as path
import cv2





if __name__ == "__main__":
  img_files = glob.glob(path.join(path.dirname(__file__),'./images/*.jpg'))


  if not img_files:
    print("No Images")
    sys.exit()
    



  WIN = 'image'

  cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)
  cv2.setWindowProperty(WIN, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)



  cnt = len(img_files)
  idx = 0

  while True:
    img = cv2.imread(img_files[idx])         
    
    if img is None:
      print("Image Load Failed")
      sys.exit()    
    cv2.imshow(WIN, img)        
    if cv2.waitKey(2000) == 27: break
    
    idx+=1
    if idx==cnt : idx=0
    

  cv2.destroyWindow(WIN)    
    
  
  
  
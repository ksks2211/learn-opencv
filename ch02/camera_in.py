import sys
import cv2

cap = cv2.VideoCapture('ch02/video/video1.mp4')

if not cap.isOpened():
  print("Camera open failed")
  sys.exit()
  
  
print('Frame Width : ', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Frame height : ',cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print('Frame Per Second : ',cap.get(cv2.CAP_PROP_FPS))


while True:    
  ret, frame = cap.read()
  if not ret:
    break
  
  cv2.imshow('frame',frame)
  
  # edge = cv2.Canny(frame, 50,150)
  # cv2.imshow('edge',edge)
  if cv2.waitKey(20) == 27:  # wait for 20ms
    break 
    
  
cap.release()  
cv2.destroyAllWindows()
  
  
  
  
    
  
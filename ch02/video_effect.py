import cv2
import numpy as np


cap1 = cv2.VideoCapture('ch02/video/video1.mp4')

cap2 = cv2.VideoCapture('ch02/video/video2.mp4')


#cap1
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS) # 초당 프레임수


#cap2
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))



out = cv2.VideoWriter('ch02/video/output-dissolve.avi',cv2.VideoWriter_fourcc(*'DIVX'),fps,(w,h))

effect_frames = int(fps* 2) # 전환되는 프레임수 2초간 전환
delay = int(1000/fps)  # 프레임간 딜레이




for i in range(frame_cnt1 - effect_frames):
    ret1 , frame1 = cap1.read()
    if not ret1: break
    out.write(frame1)
    cv2.imshow('frame',frame1)
    cv2.waitKey(delay)

# 2초 - 밀기 전환
# for i in range(effect_frames):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()

#     dx = round(w / effect_frames * i)
#     frame = np.hstack((frame2[:,:dx],frame1[:,dx:]))
#     out.write(frame)
#     cv2.imshow('frame',frame)
#     cv2.waitKey(delay)

# 2초 - dissolve
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    alpha = 1 - i/(effect_frames-1)
    frame = cv2.addWeighted(frame1, alpha, frame2, 1-alpha,0)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.waitKey(delay) 




for i in range(effect_frames,frame_cnt2):
    ret2 , frame2 = cap2.read()
    out.write(frame2)
    cv2.imshow('frame',frame2)
    cv2.waitKey(delay)

out.release()
cap1.release()
cap2.release()

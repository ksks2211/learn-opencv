import numpy as np



level = np.ones((240,480,3),dtype=np.uint8)*2000
level = np.clip(level, 0,255)

print(level)
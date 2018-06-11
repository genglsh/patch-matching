import cv2
import os
import numpy as np
import time

photo = cv2.imread(os.path.join('photo', '1.png'))
photo_gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
print(photo_gray)
# cv2.imshow('after', photo_gray)
print(photo.shape)      
ret, photo_inv = cv2.threshold(photo_gray, 13, 1, cv2.THRESH_BINARY)
print(photo_inv.shape)  
print(photo_inv)
cv2.imshow('binary', photo_inv)
time.sleep(5)
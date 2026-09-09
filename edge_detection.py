import os
import cv2
import numpy as np
img =cv2.imread(os.path.join('.','football player.jpg'))
img_edged= cv2.Canny(img,100,200)
img_edged_d=cv2.dilate(img_edged,np.ones((5,5),np.int8))
img_edged_e=cv2.erode(img_edged_d,np.ones((5,5),np.int8))

cv2.imshow('image',img)
cv2.imshow('edged_image',img_edged)
cv2.imshow('dilated_edged_image',img_edged_d)
cv2.imshow('eroded_edged_image',img_edged_e)
cv2.waitKey(0)
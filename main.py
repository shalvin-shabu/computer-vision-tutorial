import os 
import cv2
img=cv2.imread(os.path.join('.','bird.jpg'))
new_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('image',img)
cv2.imshow('new_image',new_img)
cv2.imshow('gray_image',img_gray)
cv2.imshow('hsv_image',img_hsv)

cv2.waitKey(0)  
 
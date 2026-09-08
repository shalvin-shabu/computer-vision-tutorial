import os 
import cv2 
img=cv2.imread(os.path.join('.','bird.jpg'))
k_size=11
img_blur=cv2.blur(img,(k_size,k_size))
img_gaussian=cv2.GaussianBlur(img,(k_size,k_size),5)
img_median=cv2.medianBlur(img,k_size)
cv2.imshow('image',img)
cv2.imshow('blurred_image',img_blur)
cv2.imshow('gaussian_blurred_image',img_gaussian)
cv2.imshow('median_blurred_image',img_median)
cv2.waitKey(0)
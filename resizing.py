import os 
import cv2
img=cv2.imread(os.path.join('.','bird.jpg'))
resize_img=cv2.resize(img,(306,204))
print(img.shape)
print(resize_img.shape)
cv2.imshow('image',img)

cv2.imshow('resized image',resize_img)
cv2.waitKey(0)
import os 
import cv2
img= cv2.imread(os.path.join('.','images (1).jpg'))
print(img.shape)
#line
cv2.line(img,(100,150),(300,45),(0,255,0),5)

#rectangle
cv2.rectangle(img,(100,150),(300,45),(0,255,0),5)


#circle



#text


cv2.imshow('image',img)
cv2.waitKey(0)
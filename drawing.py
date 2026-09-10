import os 
import cv2
img= cv2.imread(os.path.join('.','images (1).jpg'))
print(img.shape)
#line
cv2.line(img,(100,150),(300,45),(0,255,0),5)

#rectangle
cv2.rectangle(img,(200,150),(300,45),(0,0,255),-1)


#circle
cv2.circle(img,(200,300),15,(255,0,0),10)


#text
cv2.putText(img,'hi',(100,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2 )

cv2.imshow('image',img)
cv2.waitKey(0)
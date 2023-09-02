import cv2
import numpy as np
kernel=np.ones((3,3),np.uint8)
img=cv2.imread('test_img.jpeg')
imgDailation=cv2.dilate(img,kernel,iterations=1)
Erodedimg=cv2.erode(imgDailation,kernel,iterations=2)
cv2.imshow("Dialation Image",imgDailation)
cv2.imshow("Eroded image",Erodedimg)
cv2.waitKey(0)

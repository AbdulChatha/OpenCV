import cv2
import numpy as np
img=cv2.imread("test_img.jpeg")
imgHor=np.hstack((img,img))
imgVtcl=np.vstack((img,img))
cv2.imshow("Vertical Join",imgVtcl)
cv2.imshow("Horizontal Join",imgHor)
cv2.waitKey(0)
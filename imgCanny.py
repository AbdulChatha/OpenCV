import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
img=cv2.imread("test_img.jpeg")
imgCanny=cv2.Canny(img,10,200)
cv2.imshow("image",img)
cv2.imshow("Canny Image",imgCanny)
cv2.waitKey(0)

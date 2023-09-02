import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
# img[:]=255,200,150
# cv2.line(img,(0,0),(200,200),(0,255,0))
# cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(255,0,150))
# cv2.rectangle(img,(150,150),(250,300),(255,0,150))
cv2.circle(img,(200,200),100,(255,0,150),cv2.FILLED)
cv2.putText(img,"OpenCV",(150,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,250,150),1)
cv2.imshow("Image",img)

cv2.waitKey(0)
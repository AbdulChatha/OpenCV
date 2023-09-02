import cv2
import numpy as np
def color_detection(image_path,color_range):
    img=cv2.imread(image_path)
    hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_bound=np.array(color_range[0])
    upper_bound=np.array(color_range[1])
    mask=cv2.inRange(hsv_img,lower_bound,upper_bound)
    result=cv2.bitwise_and(img,img,mask=mask)
    return result
blue_range = ([100, 50, 50], [130, 255, 255])
image_path="lambo blue.jpeg"
cv2.imshow("oringnal image",cv2.imread(image_path))
cv2.imshow("Color Detection",color_detection(image_path,blue_range))
cv2.waitKey(0)

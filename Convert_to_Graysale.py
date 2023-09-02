import cv2
img=cv2.imread("test_img.jpeg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)
imgBlur=cv2.GaussianBlur(img,(7,7),0) #(7,7) kernel size in x,y direction, 0 is standard daviation of Gaussian
cv2.imshow('Blur Image',imgBlur)     # if standard daviation of Gaussian is 0 then it will be auto adjust else ..
cv2.waitKey(0)
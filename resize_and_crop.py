import cv2
img=cv2.imread("test_img.jpeg")
print(img.shape)
resized_img=cv2.resize(img,(500,600))
print(resized_img.shape)
croped_img=img[20:150,10:200]
# cv2.imshow(" resized image",resized_img)
cv2.imshow("Croped Image",croped_img)
cv2.imshow("Image",img)
cv2.waitKey(0)
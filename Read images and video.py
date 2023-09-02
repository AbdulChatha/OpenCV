import cv2
##reading image
# img=cv2.imread('test_img.jpeg')
# cv2.imshow('Image',img)
# cv2.waitKey(0) #if 0 then infinite wait, if any positive number then in miliseconds
##reading video
# cap = cv2.VideoCapture('taking off.mp4')

# while True:
#     success, img = cap.read()
#     cv2.imshow('video', img)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # Modified condition
#         break

# webcam
cap = cv2.VideoCapture(0)
cap.set(3,200) #width
cap.set(4,300) #hieght
# cap.set(10,1000) #brightness
while True:
    success, img = cap.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

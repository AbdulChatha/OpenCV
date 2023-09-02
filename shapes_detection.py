import cv2
def getCounters(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        # print(area)
        peri=cv2.arcLength(cnt,True)
        # print(peri)
        aprox=cv2.approxPolyDP(cnt,0.02*peri,True)
        # print(len(aprox))
        x,y,w,h=cv2.boundingRect(aprox)
        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.drawContours(imgContour,cnt,-1,(255,0,0),2)
        objcor=len(aprox)
        if objcor==3: objectType="Tri"
        elif objcor==4:
            aspratio=w/float(h)
            if aspratio >0.95 and aspratio <1.05:
                objectType="Square"
            else:
                objectType="rectangle"
        else:
            objectType='Circle'
        cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
img=cv2.imread("shapes.png")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny=cv2.Canny(imgGray,50,50)
imgContour=img.copy()
getCounters(imgCanny)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Contours",imgContour)
cv2.waitKey(0)
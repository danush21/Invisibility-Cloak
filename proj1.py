import numpy as np
import cv2
cap=cv2.VideoCapture("vid1.mp4")
bg=cv2.imread("pic1.jpg")
while 1:
    ret, frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([80,0,0])
    upper=np.array([180,255,255])
    mask1=cv2.inRange(hsv,lower,upper)
    lower=np.array([0,0,0])
    upper=np.array([2,255,255])
    mask3=cv2.inRange(hsv,lower,upper)
    mask1=mask1+mask3
    mask1=cv2.erode(mask1,np.ones((5,5),np.uint8),iterations=2)
    mask1=cv2.dilate(mask1,np.ones((5,5),np.uint8),iterations=2)
    mask2=cv2.bitwise_not(mask1)
    res=cv2.bitwise_and(bg,bg,mask=mask1)
    res1=cv2.bitwise_and(frame,frame,mask=mask2)
    video=res+res1
    cv2.imshow("video",video)
    k=cv2.waitKey(3)
    if k==27:
        break
cv2.destroyAllWindows() 

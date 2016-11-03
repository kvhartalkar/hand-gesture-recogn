import cv2                              
import numpy as np
hul=0
cap = cv2.VideoCapture(0)               
while( cap.isOpened() ) :
    ret,img = cap.read()                         
    cv2.imshow('input',img)                  
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray',gray)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #cv2.imshow('blur',blur)
    ret,thresh1 = cv2.threshold(gray,127,255,0)
    #cv2.imshow('thresh',thresh1)
    gray,contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    max_area =1
    ci=0
    for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
    cnt=contours[ci]
    #print 'max area'
    #print max_area
    hull = cv2.convexHull(cnt)
    hul=cv2.contourArea(hull)
    print 'HULL',hul
    cv2.drawContours(img,[cnt],0,(0,255,0),2)
    cv2.drawContours(img,[hull],0,(0,0,255),2)
    ellipse = cv2.fitEllipse(cnt)
    img = cv2.ellipse(img,ellipse,(0,255,0),2)
    cv2.imshow('draw',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

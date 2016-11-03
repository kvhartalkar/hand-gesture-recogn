import cv2                              
import numpy as np
import time
#VARIABLE DEC
cntr=0
hull_area=0
solidity=0
k=0
text1=''
a=['']
text=['']
perimeter_count=0
perimeter_hull=0

#ARRAY DEC
cntar=np.zeros((10))
hular=np.zeros((10))
soli=np.zeros((10))
pericnt=np.zeros((10))
perihul=np.zeros((10))
#FILE DEC

val=np.zeros((10))
cap = cv2.VideoCapture(0)               
while( cap.isOpened() ) :
    while(True):
        ret,im=cap.read()
        cv2.imshow('INPUT',im)
        if cv2.waitKey(1) & 0xFF == ord('n'):
            break
    
    
    ret,img = cap.read()                         
    cv2.imshow('input',img)                  
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray',gray)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #cv2.imshow('blur',blur)
    ret,thresh1 = cv2.threshold(gray,127,255,0)
    #cv2.imshow('thresh',thresh1)
    gray,contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    max_area1 =1
    ci=0
    for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area1):
                max_area1=area
                ci=i
    cnt=contours[ci]
    #CONTOUR AREA
    #max_area1
    #HULL AREA
    hull = cv2.convexHull(cnt)
    hull_area=cv2.contourArea(hull)
    #hull_area
    #SOLIDITY
    solidity=max_area1/hull_area
    #solidity
    #PERIMETER
    perimeter_count=cv2.arcLength(cnt,True)
    #perimeter_count    
    perimeter_hull=cv2.arcLength(hull,True)
    #perimeter_hull
    #print "ENTER WHAT TO SAY!!"
    #text1=raw_input()
    #text[cntr]=text1
    

    print 'max area',max_area1
    print 'hull area',hull_area
    print 'solidity',solidity
    print 'peri cnt',perimeter_count
    print 'peri hull',perimeter_hull




    #DRAW CONTOURS
    cv2.drawContours(img,[cnt],0,(0,255,0),2)
    cv2.drawContours(img,[hull],0,(0,0,255),2)
    ellipse = cv2.fitEllipse(cnt)
    img = cv2.ellipse(img,ellipse,(0,255,0),2)
    cv2.imshow('draw',img)
     
    
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()



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
cntar=np.zeros((20))
hular=np.zeros((20))
soli=np.zeros((20))
pericnt=np.zeros((20))
perihul=np.zeros((20))
#FILE DEC

val=np.zeros((20))
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
    cv2.imshow('gray',gray)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    cv2.imshow('blur',blur)
    ret,thresh1 = cv2.threshold(gray,70,82,1)
    cv2.imshow('thresh',thresh1)
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
    cntar[cntr]=max_area1
    #HULL AREA
    hull = cv2.convexHull(cnt)
    hull_area=cv2.contourArea(hull)
    hular[cntr]=hull_area
    #SOLIDITY
    solidity=max_area1/hull_area
    soli[cntr]=solidity
    #PERIMETER
    perimeter_count=cv2.arcLength(cnt,True)
    pericnt[cntr]=perimeter_count    
    perimeter_hull=cv2.arcLength(hull,True)
    perihul[cntr]=perimeter_hull
    #print "ENTER WHAT TO SAY!!"
    #text1=raw_input()
    #text[cntr]=text1
    
    #SAVE GESTURE
    cv2.imwrite('gesture'+str(cntr)+'.jpeg',img)
    #print 'max area',max_area1
    #print 'hull area',hull_area
    #print 'solidity',solidity
    #print 'peri cnt',perimeter_count
    #rint 'peri hull',perimeter_hull




    #DRAW CONTOURS
    cv2.drawContours(img,[cnt],0,(0,255,0),2)
    cv2.drawContours(img,[hull],0,(0,0,255),2)
    ellipse = cv2.fitEllipse(cnt)
    img = cv2.ellipse(img,ellipse,(0,255,0),2)
    cv2.imshow('draw',img)
    cv2.imwrite('count'+str(cntr)+'.jpeg',img)
    cntr=cntr+1

     
    
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
    #SAVE TO FILE
np.savetxt('hullarea.txt',hular,delimiter=",",fmt="%f")
np.savetxt('contarea.txt',cntar,delimiter=",",fmt="%f")
np.savetxt('solidity.txt',soli,delimiter=",",fmt="%f")
np.savetxt('contperi.txt',pericnt,delimiter=",",fmt="%f")
np.savetxt('hullperi.txt',perihul,delimiter=",",fmt="%f")
#np.savetxt('cntr.txt',cntr,fmt="%d")
#print 'max area',cntar
#print 'hull area',hular
#print 'solidity',soli
#print 'peri cnt',pericnt
#print 'peri hull',perihul

cap.release()
cv2.destroyAllWindows()

    #FILE DATA DISPLAY
#val=np.loadtxt('hullarea.txt',dtype=float,delimiter=",")
#print 'hullarea',val
#val=np.loadtxt('contarea.txt',dtype=float,delimiter=",")
#print 'contarea',val
#val=np.loadtxt('solidity.txt',dtype=float,delimiter=",")
#print 'solidity',val
#val=np.loadtxt('contperi.txt',dtype=float,delimiter=",")
#print 'contperi',val
#val=np.loadtxt('hullperi.txt',dtype=float,delimiter=",")
#print 'hullperi',val


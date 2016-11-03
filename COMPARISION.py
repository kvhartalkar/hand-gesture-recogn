#COMPARISION
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    ret,frame =cap.read()
    cv2.imshow('cap',frame)
    print "1st in "
    #if cv2.waitKey(1) & 0xFF == ord('n'):
    break
print "1st out"
cv2.destroyAllWindows()
textarr=list('')
hull_area=np.zeros((10))
count_area=np.zeros((10))
pericnt=np.zeros((10))
perihul=np.zeros((10))
solidity=np.zeros((10))
cntr1=0
k=0
i=0
print 'ENTER TOTAL GESTURES'
i=raw_input()

    

    #FILE DATA DISPLAY
hull_area=np.loadtxt('hullarea.txt',dtype=float,delimiter=",")
print 'hullarea',hull_area
count_area=np.loadtxt('contarea.txt',dtype=float,delimiter=",")
print 'contarea',count_area
solidity=np.loadtxt('solidity.txt',dtype=float,delimiter=",")
print 'solidity',solidity
pericnt=np.loadtxt('contperi.txt',dtype=float,delimiter=",")
print 'contperi',pericnt
perihul=np.loadtxt('hullperi.txt',dtype=float,delimiter=",")
print 'hullperi',perihul
textarr=np.loadtxt('text.txt',dtype=np.str,delimiter=" ")
print 'text file',textarr

    #CREATING MAX AND MIN RANGE
#MAX ARRAY
hull_area_max=np.zeros((10))
count_area_max=np.zeros((10))
pericnt_max=np.zeros((10))
perihul_max=np.zeros((10))
solidity_max=np.zeros((10))
#MIN ARRAY
hull_area_min=np.zeros((10))
count_area_min=np.zeros((10))
pericnt_min=np.zeros((10))
perihul_min=np.zeros((10))
solidity_min=np.zeros((10))

#SAVE VALUE IN MAX & MIN
for cntr in range (int(i)):
    k=(hull_area[cntr]*3)/100
    hull_area_max[cntr]=hull_area[cntr]+k
    k=(count_area[cntr]*3)/100
    count_area_max[cntr]=count_area[cntr]+k
    k=(pericnt[cntr]*3)/100
    pericnt_max[cntr]=pericnt[cntr]+k
    k=(perihul[cntr]*3)/100
    perihul_max[cntr]=perihul[cntr]+k
    k=(solidity[cntr]*3)/100
    solidity_max[cntr]=solidity[cntr]+k
print 'MAX VALUE CALCULATED'
print 'hull_area_max',hull_area_max
print 'count_area_max',count_area_max
print 'pericnt_max',pericnt_max
print 'perihul_max',perihul_max
print 'solidity_max',solidity_max


for cntr in range (int(i)):
    k=(hull_area[cntr]*3)/100
    hull_area_min[cntr]=hull_area[cntr]-k
    k=(count_area[cntr]*3)/100
    count_area_min[cntr]=count_area[cntr]-k
    k=(pericnt[cntr]*3)/100
    pericnt_min[cntr]=pericnt[cntr]-k
    k=(perihul[cntr]*3)/100
    perihul_min[cntr]=perihul[cntr]-k
    k=(solidity[cntr]*3)/100
    solidity_min[cntr]=solidity[cntr]-k
print 'MIN VALUE CALCULATED'
print 'hull_area_min',hull_area_min
print 'count_area_min',count_area_min
print 'pericnt_min',pericnt_min
print 'perihul_min',perihul_min
print 'solidity_min',solidity_min

print "#########start"
#REAL TIME GESTURE VALUES
while( cap.isOpened() ) :
    while(True):
        ret,im=cap.read()
        print "2nd in"
        cv2.imshow('INPUT1',im)
        if cv2.waitKey(1) & 0xFF == ord('n'):
            break
    print "2nd out"   
    
    ret,img = cap.read()                         
    cv2.imshow('compare',img)                  
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
    hull_area1=cv2.contourArea(hull)
    #hull_area
    #SOLIDITY
    solidity=max_area1/hull_area
    #solidity
    #PERIMETER
    perimeter_count=cv2.arcLength(cnt,True)
    #perimeter_count    
    perimeter_hull=cv2.arcLength(hull,True)
    #perimeter_hull

#COMPARE WITH STORED VALUES
    flag=0
    for j in range(int(i)):
        if hull_area_min <=  hull_area1 <= hull_area_max :
            flag=flag+1
        if count_area_min <=  max_area1 <= count_area_max :
            flag=flag+1
        if pericnt_min <=  perimeter_count <= pericnt_max :
            flag=flag+1
        if perihul_min <=  perimeter_hull <= perihul_max :
            flag=flag+1
        if solidity_min <=  solidity <= solidity_max :
            flag=flag+1
    print "flag=" , flag


    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
    
cap.release()
cv2.destroyAllWindows()

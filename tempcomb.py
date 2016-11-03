#COMPARISION
import cv2
import numpy as np
import pyttsx
engine=pyttsx.init()
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
j=0
say=list('')
hull_area=0
count_area=0
pericnt=0
perihul=0
solidity1=0
cntr1=0
k=0
i=0
lim=5
print 'ENTER TOTAL GESTURES'
i=raw_input()
flag=np.zeros((int(i)))
cn=i    

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
hull_area_max=np.zeros((20))
count_area_max=np.zeros((20))
pericnt_max=np.zeros((20))
perihul_max=np.zeros((20))
solidity_max=np.zeros((20))
#MIN ARRAY
hull_area_min=np.zeros((20))
count_area_min=np.zeros((20))
pericnt_min=np.zeros((20))
perihul_min=np.zeros((20))
solidity_min=np.zeros((20))

#SAVE VALUE IN MAX & MIN
for cntr in range (int(i)):
    k=(hull_area[cntr]*lim)/100
    hull_area_max[cntr]=hull_area[cntr]+k
    k=(count_area[cntr]*lim)/100
    count_area_max[cntr]=count_area[cntr]+k
    k=(pericnt[cntr]*lim)/100
    pericnt_max[cntr]=pericnt[cntr]+k
    k=(perihul[cntr]*lim)/100
    perihul_max[cntr]=perihul[cntr]+k
    k=(solidity[cntr]*lim)/100
    solidity_max[cntr]=solidity[cntr]+k
print 'MAX VALUE CALCULATED'
print 'hull_area_max',hull_area_max
print 'count_area_max',count_area_max
print 'pericnt_max',pericnt_max
print 'perihul_max',perihul_max
print 'solidity_max',solidity_max


for cntr in range (int(i)):
    k=(hull_area[cntr]*lim)/100
    hull_area_min[cntr]=hull_area[cntr]-k
    k=(count_area[cntr]*lim)/100
    count_area_min[cntr]=count_area[cntr]-k
    k=(pericnt[cntr]*lim)/100
    pericnt_min[cntr]=pericnt[cntr]-k
    k=(perihul[cntr]*lim)/100
    perihul_min[cntr]=perihul[cntr]-k
    k=(solidity[cntr]*lim)/100
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
        #print "2nd in"
        cv2.imshow('INPdUTss1S2',im)
        if cv2.waitKey(1) & 0xFF == ord('n'):
            break
    #print "2nd out"   
    
    ret,img = cap.read()                         
    #cv2.imshow('compaSre1',img)                  
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray',gray)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #cv2.imshow('blur',blur)
    ret,thresh1 = cv2.threshold(gray,70,82,1)
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
    solidity1=max_area1/hull_area1
    #solidity
    #PERIMETER
    perimeter_count=cv2.arcLength(cnt,True)
    #perimeter_count    
    perimeter_hull=cv2.arcLength(hull,True)
    #perimeter_hull

    #DRAW CONTOURS
    cv2.drawContours(img,[cnt],0,(0,255,0),2)
    cv2.drawContours(img,[hull],0,(0,0,255),2)
    ellipse = cv2.fitEllipse(cnt)
    img = cv2.ellipse(img,ellipse,(0,255,0),2)
    cv2.imshow('dradw',img)
     

###VALUES CALCULATED
    print 'max area',max_area1
    print 'hull area',hull_area1
    print 'solidity',solidity1
    print 'peri cnt',perimeter_count
    print 'peri hull',perimeter_hull

     
#COMPARE WITH STORED VALUES
    flag=np.zeros((int(cn)))
    for j in range(int(cn)):
        print "gesture=",j
        if hull_area_min[j] <=  hull_area1 <= hull_area_max[j] :
            flag[j]=flag[j]+1
            print "hull"
        if count_area_min[j] <=  max_area1 <= count_area_max[j] :
            flag[j]=flag[j]+1
            print "max area"
        if pericnt_min[j] <=  perimeter_count <= pericnt_max[j] :
            flag[j]=flag[j]+1
            print "pericount"
        if perihul_min[j] <=  perimeter_hull <= perihul_max[j] :
            flag[j]=flag[j]+1
            print "peri hull"
        if solidity_min[j] <=  solidity1 <= solidity_max[j] :
            flag[j]=flag[j]+1
            print "solidity"
    m=0        
    print "flag=" , flag
    if cv2.waitKey(1) & 0xFF == ord('q') :
            break 
    m=np.amax(flag)
    cntr1=0
    while(flag[cntr1]!=m):
        cntr1=cntr1+1
    if m>=3 and m<=cn:
        print 'max index',m
    #if cv2.waitKey(1) & 0xFF == ord('s') :
        #print 'SAY',say
    #if m!=0 & m<=cn:
        say.append((textarr[cntr1]))
        np.savetxt('say.txt',say,delimiter=" ",fmt="%s")
        print 'SAY',say
    else :  
        print 'no success'
print 'Say text file',say
audio=' , '.join(say)
print 'Audio sentencce',audio
engine.say(audio)
engine.runAndWait()
audio=''
cap.release()
cv2.destroyAllWindows()


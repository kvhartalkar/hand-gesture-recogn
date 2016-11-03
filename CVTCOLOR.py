import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while(True):
    ret,fr=cap.read()
    #CONVERCOLOR
    gray=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    cv2.imshow('frame',fr)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

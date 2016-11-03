import cv2
import numpy as np
temp_text=list('')
load=list('')

print 'ENTER TOTAL SHOWN GESTURES'
total=raw_input()
print 'ENTER TEXT ACCORDINGLY'
for i in range(int(total)):
    n=raw_input()
    temp_text.append((n))
    
print temp_text
temp_text=''
print 'tem=',temp_text


l=np.ones((5))
print 'l=',l

l=np.zeros((5))

print 'l==',l


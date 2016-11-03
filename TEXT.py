#TAKE TEXT FROM USER
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
np.savetxt('text.txt',temp_text,delimiter=" ",fmt="%s")
load=np.loadtxt('text.txt',dtype=np.str,delimiter=" ")
print load



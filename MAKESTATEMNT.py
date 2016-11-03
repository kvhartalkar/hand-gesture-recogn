import pyttsx
import numpy as np
engine=pyttsx.init()
load=list('')
load=np.loadtxt('say.txt',dtype=np.str,delimiter=" ")

#print 'ENTER TOTAL SHOWN GESTURES'
#total=raw_input()
#print 'ENTER TEXT ACCORDINGLY'
#for i in range(int(total)):
#    n=raw_input()
#    b.append((n))
print load
k=' '.join(load)
print k
engine.say(k)
engine.runAndWait()
k=''
print 'k=',k

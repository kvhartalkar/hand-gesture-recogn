import pyttsx
import numpy as np
arr=np.zeros((10))
val=np.zeros((10))
siz=raw_input("Size of array")
print 'enter nos'
for i in range (int(siz)):
    n=raw_input()
    arr[i]=n
#np.savetxt('temp.txt',arr,delimiter=",",fmt="%d")
np.savetxt('temp.txt',arr,delimiter=",",fmt="%f")
val=np.loadtxt('temp.txt',dtype=float,delimiter=",")
#val=np.loadtxt('temp.txt',dtype=int,delimiter=",")
print arr
print val

val=np.loadtxt('hullarea.txt',dtype=float,delimiter=",")
print 'hullarea',val
val=np.loadtxt('contarea.txt',dtype=float,delimiter=",")
print 'contarea',val
val=np.loadtxt('solidity.txt',dtype=float,delimiter=",")
print 'solidity',val
val=np.loadtxt('contperi.txt',dtype=float,delimiter=",")
print 'contperi',val
val=np.loadtxt('hullperi.txt',dtype=float,delimiter=",")
print 'hullperi',val

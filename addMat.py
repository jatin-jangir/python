import numpy as np
def AddMat(a,b):
    for i in range(0,len(a)):
         a[i]=a[i]+b[i]
    return a

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[9,8,7],[6,5,4],[3,2,1]])
C=AddMat(A,B)
print (C)
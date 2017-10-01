#SVM Assignemnt For Slide Hinge Loss
import numpy
from numpy import random

def LoadData():
    Name=input("Please input the DataSet's Full Name(XXX.txt):\n")
    Path='./DataSet/'+ Name
    Data=numpy.loadtxt(Path)
    return Data

def Hinge(Y,W,X):
    Temp=1-numpy.dot(Y,numpy.dot(W.transpose(),X))
    if(Temp>=0):
        return Temp
    else:
        return 0

#m=59535,157413,271617;n=8, for DataSet:Train,Unused,Validation sepecificly.
m=input("Please input the Columns:\n")
n=input("Please input the Rows:\n")
m=int(m)
n=int(n)
Data=LoadData()
Y=Data[:,0].reshape(m,1)

X0=numpy.zeros(1,n)
X=Data[:,1:n+1]
X=numpy.row_stack(X0,X)

W=numpy.random.random(size=(n+1,1))
W[0,0]=1
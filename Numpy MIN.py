import numpy as np
def minnp(a,b):
    #Returns Minimum of adding of a + b
    d1=a.shape
    d2=b.shape
    min1=(min(d1[0],d2[0]))
    min2=(min(d1[1],d2[1]))
    c1=np.zeros((min1,min2))
    for x1 in range(min1):
        for x2 in range(min2):
            c1[x1,x2]=a[x1,x2]+b[x1,x2]
    return c1 #the result

a=np.array([[2,5,9],[3,8,6]])
b=np.array([[1,2,6,5]])
print (minnp(a,b)) #print the result
import numpy as np
def maxnp(a,b):
    #returns Max adding of a + b
    d1=a.shape
    d2=b.shape
    max1=(max(d1[0],d2[0]))
    max2=(max(d1[1],d2[1]))
    c1=np.zeros((max1,max2))
    for x1 in range(d1[0]):
        for x2 in range(d1[1]):
            c1[x1,x2]= c1[x1,x2]+ a[x1,x2]
    for x1 in range(d2[0]):
        for x2 in range(d2[1]):
            c1[x1,x2] = c1[x1,x2] + b[x1,x2]
    return c1 #the result
    
a=np.array([[2,5,7],[3,8,6]])
b=np.array([[1,2,6,5]])
print (maxnp(a,b)) #print the result
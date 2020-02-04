import numpy as np
def mission(a,b):
    #function gets 2 Matrixes a,b
    #returns the result of matrix multiplication a*b. if not possible, returns a message.
    d1=a.shape
    d2=b.shape
    if ((d1[0]!=d2[1]) and (d2[0]!=d1[1])):
        return 'cannot be multiplied'
    if(d1[0]==d2[1]): #if a number rows = b number columns
        dRow=d2[0] #b number rows
        dColumn=d1[1]#a number columns
        c=np.zeros((dRow,dColumn)) #b rows, a columns
        d=d1[0] #the same number in a,b
        for x1 in range(dRow):
            for x2 in range(dColumn):
                #specific place c[x1,x2]
                for x3 in range(d):
                    c[x1,x2]=c[x1,x2] + (a[x3,x2] * b[x1,x3])
                    
    if(d1[1]==d2[0]): #if b number rows = a number columns
        dRow=d1[0] #a number rows
        dColumn=d2[1] #b number Columns
        c=np.zeros((dRow,dColumn)) #a rows, b columns
        d=d1[1] #the same number in a,b
        for x1 in range(dRow):
            for x2 in range(dColumn):
                #specific place c[x1,x2]
                for x3 in range(d):
                    c[x1,x2]=c[x1,x2] + (a[x1,x3] * b[x3,x2])#each time adds the Multiplication to the number
    return c

a=np.array([[2,5,7], [3,8,6],[5,8,2],[1,6,1]]) #4 rows, 3 columns
b=np.array([[1,2,6,5]]) #1 row, 4 columns
print ('result of matrix multiplication a*b is:')
print (mission(a,b)) #print the result

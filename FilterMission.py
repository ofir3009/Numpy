import numpy as np
#one column right until end of row
#then one row down and repeat until last row
def Mission(a, Filter):
    b=a.shape #for moving rows and columns
    res=np.zeros((b[0]-2,b[1]-2)) #creating the array we will return
    for j in range(b[0]-2): #a.shape[0] is row number, at the end of every for we move down
        for i in range(b[1]-2): #a.shape[1] is column number, at the end of every for we move right
            res1=np.dot(a[j:j+3,i:i+3], Filter) #the multiplication
            for k in range(3):
                for z in range(3):
                    res[j,i]=res[j,i] + res1[k,z] #enter the multiplication results to the array
    return res #return the array
  
Filter=np.random.rand(3,3) 
a=np.random.uniform(low=0.0,high=5.0,size=(8,8)) #create np.array with numbers from 0.0 to 5.0
b=Mission(a,Filter) #6x6 result
print ("6x6 Result: ")
print(b)
c=Mission(b,Filter) #4x4 result
print("4x4 Result: ")
print(c)
d=Mission(c,Filter) #2x2 result
print ("2x2 Result: ")
print (d)
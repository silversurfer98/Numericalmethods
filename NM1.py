# solve simple 3 equation system
import numpy as np

m = []
m1 = []
s = int(input("enter the number of equation system :  "))
for i in range(0, s):
    a = []
    print("enter x",i+1," coeff :")
    for j in range(0, 3): 
        ele = int(input()) 
        a.append(ele)
    m.append(a)
    print("enter eq end of equation",i+1,": ")
    el = int(input())
    m1.append(el)

x = np.array(m)
z = np.array(m1)
z = z.reshape(s,1)
y = np.linalg.inv(x) 
#print(y)
#print(z)
print(np.matmul(y,z)) 


 
# solve simple 3 equation system
import numpy as np
import sys
sys.tracebacklimit=0

m = []
m1 = []
s = int(input("enter the number of equation system :  "))
for i in range(0, s):
    a = []
    print("enter x",i+1," coeff :")
    for j in range(0, s): 
        ele = int(input()) 
        a.append(ele)
    m.append(a)
    print("enter eq end of equation",i+1,": ")
    el = int(input())
    m1.append(el)

x = np.array(m)
z = np.array(m1)
z = z.reshape(s,1)
try:
    y = np.linalg.inv(x)
    ans = np.matmul(y,z)
    for i in range(0,s):
        print("\nx",i+1, ": ",ans[i])
    #print(ans) 
except:
    print("\n\n")
    print("*******************************************")
    print("solution is not convergeble") 
    print("*******************************************")
    print("\n\n")



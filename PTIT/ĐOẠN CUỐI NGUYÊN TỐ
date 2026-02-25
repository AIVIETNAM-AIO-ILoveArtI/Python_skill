import math
sang = [0]*1000000
def nt():
    sang[0]=1
    sang[1]=1
    for i in range(2,1001):
        for j in range(i+i,1000000,i):
            sang[j]=1
nt()
t = int(input())
for i in range(t):
    s = input()
    g = int(s[-4::])
    if sang[g]==0:
        print("YES")
    else:
        print("NO")

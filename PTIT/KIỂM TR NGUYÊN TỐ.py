import math
sang = [0]*10000
def nt():
    sang[0]=1
    sang[1]=1
    for i in range(2,101):
        for j in range(i+i,10000,i):
            sang[j]=1
nt()
t = int(input())
for i in range(t):
    s = input()
    so = int(s[-4::])
    if sang[so]==0:
        print("YES")
    else:
        print("NO")

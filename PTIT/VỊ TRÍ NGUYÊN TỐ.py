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
    n = input()
    dko = True
    for j in range(len(n)):
        if sang[j]==0:
            if sang[int(n[j])]==1:
                dko = False
        else:
            if sang[int(n[j])]==0:
                dko = False
    if dko:
        print("YES")
    else:
        print("NO")

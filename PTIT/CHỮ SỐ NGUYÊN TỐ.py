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
    if sang[len(n)]!=0:
        dko = False
    nt =0
    knt = 0
    for i in range(len(n)):
        if sang[int(n[i])]==0:
            nt+=1
        else:
            knt+=1
    if nt<=knt:
        dko = False
    if dko:
        print('YES')
    else:
        print('NO')


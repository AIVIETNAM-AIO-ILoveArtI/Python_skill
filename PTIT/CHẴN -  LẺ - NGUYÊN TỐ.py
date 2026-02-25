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
    tong =0
    for j in range(0,len(n),2):
        if int(n[j])%2!=0:
            dko = False
        tong += int(n[j])
    for j in range(1, len(n), 2):
        if int(n[j])%2==0:
            dko = False
        tong += int(n[j])
    if sang[tong]==0 and dko:
        print("YES")
    else:
        print("NO")

import math
sang = []
for i in range (100000):
    sang.append(0)
def snt():
    sang[0]=1
    sang[1]=1
    f = int(math.sqrt(100000))
    for i in range(2,f+1):
        for j in range(i+i,100000,i):
            sang[j]=1
snt()
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    c =math.gcd(a,b)
    s = str(c)
    dem =0
    for i in range(len(s)):
        dem += int(s[i])
    if sang[dem]==0:
        print('YES')
    else:
        print('NO')

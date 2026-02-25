import math
sang = []
for i in range(1,100000):
    sang.append(0)
def snt():
    sang[0]=1
    sang[1]=1
    g = int(math.sqrt(10000))
    for i in range(2,g+1,1):
        for j in range (i+i,10000,i):
            sang [j]=1

snt()
case = int(input())
for i in range(case):
    n = int(input())
    dem =0
    for j in range(n):
        if math.gcd(j,n)==1:
            dem+=1
    if sang[dem]==0:
        print('YES')
    else:
        print('NO')

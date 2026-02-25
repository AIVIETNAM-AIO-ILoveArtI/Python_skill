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
    dem =1
    for j in range(1,len(s)):
        if s[j]==s[j-1]:
            dem+=1
        else:
            print(str(dem)+s[j-1],end ='')
            dem = 1
    print(str(dem)+s[-1])

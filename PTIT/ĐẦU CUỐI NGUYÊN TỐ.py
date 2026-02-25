sang = [0]*10000
def nt():
    sang[0]=1
    sang[1]=1
    for i in range(2,100):
        for j in range(i+i,10000,i):
            sang[j]=1
t = int(input())
nt()
for i in range(t):
    s = input()
    if sang[int(s[-3::])]==0 and sang[int(s[0:3])]==0:
        print("YES")
    else:
        print("NO")

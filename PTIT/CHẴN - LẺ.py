import math
t = int(input())
for i in range(t):
    n = int(input())
    dem =0
    s = str(n)
    while n>0:
        dem += n%10
        n//=10
    dko = True
    for i in range(1,len(s)):
        a = int(s[i])
        b = int(s[i-1])
        if a>=b:
            if a-b!=2:
                dko = False
        else:
            if b-a!=2:
                dko = False
    if dko and dem%10==0:
        print('YES')
    else:
        print('NO')

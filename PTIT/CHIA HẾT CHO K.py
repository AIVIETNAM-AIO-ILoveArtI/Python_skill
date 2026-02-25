a,k,n = map(int,input().split())
g = []
dko = True
for i in range (0,n+1,k):
    if i-a>0:
        dko = False
        g.append(i-a)
if(dko):
    print('-1')
else:
    print(*g)

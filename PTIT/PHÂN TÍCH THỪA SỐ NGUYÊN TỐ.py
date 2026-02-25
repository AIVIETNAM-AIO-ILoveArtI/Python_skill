sang = [0]*1000000
def nt():
    sang[1]=1
    sang[0]=1
    for i in range(2,1001):
        for j in range(i+i,100000,i):
            sang[j]=1
nt()
snt = []
for j in range(len(sang)):
    if sang[j]==0:
        snt.append(j)
t = int(input())
for i in range(t):
    so = int(input())
    j = 0
    s = str()
    dem = 0
    while so>1:
        if so % snt[j]==0:
            so /= snt[j]
            dem+=1
        else:
            if dem>=1:
                s += ' * ' + str(snt[j]) + '^' + str(dem)
            j+=1
            dem = 0
    s += ' * ' + str(snt[j]) + '^' + str(dem)
    s = '1'+s
    print(s)

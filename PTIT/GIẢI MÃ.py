t = int(input())
for i in range(t):
    s = input()
    g=[]
    for i in range(1,len(s),2):
        for j in range(int(s[i])):
            g.append(s[i-1])
    print(*g,sep='')

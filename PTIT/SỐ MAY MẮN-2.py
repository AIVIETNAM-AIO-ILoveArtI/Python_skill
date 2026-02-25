t = int(input())

for i in range(t):
    n = int(input())
    s = str(n)
    dko = True
    for i in range(len(s)):
        if s[i]!='4'and s[i]!='7':
            dko = False
    if dko==True:
        print("YES")
    else:
        print("NO")

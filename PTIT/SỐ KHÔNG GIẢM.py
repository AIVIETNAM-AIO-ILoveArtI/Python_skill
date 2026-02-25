t = int(input())
for i in range(t):
    so = int(input())
    s = str(so)
    dko = True
    for j in range(1,len(s)):
        if s[j]<s[j-1]:
            dko = False
    if dko == True:
        print("YES")
    else:
        print("NO")

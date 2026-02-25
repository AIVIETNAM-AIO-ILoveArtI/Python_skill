t = int(input())
for i in range(t):
    s = input()
    dko = True
    cso=0
    for j in range(1,len(s)):
        if s[j]<=s[j-1]:
            cso = j
            break
    for j in range(cso,len(s)):
        if s[j]>=s[j-1]:
            dko = False
    if dko:
        print("YES")
    else:
        print("NO")

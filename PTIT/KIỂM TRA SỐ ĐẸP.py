t = int(input())
for i in range(t):
    s = input()
    dko = True
    for j in range(2,len(s),2):
        if s[j]!=s[j-2]:
            dko = False
    for j in range(3,len(s),2):
        if s[j]!=s[j-2]:
            dko = False
    if dko:
        print("YES")
    else:
        print("NO")

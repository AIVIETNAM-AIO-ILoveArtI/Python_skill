t = int(input())
for i in range(t):
    s = input()
    dko = True
    if len(s)%2==0:
        dko = False
    if s[0]==s[1]:
        dko = False
    for j in range(2,len(s),2):
        if s[j-2]!=s[j]:
            dko = False
    if s[0]!=s[-1]:
        dko = False
    if dko:
        print('YES')
    else:
        print('NO')

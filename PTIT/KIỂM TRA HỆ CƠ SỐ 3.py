t = int(input())
for i in range(t):
    s = input()
    dko = True
    for i in s:
        if i != '0' and i != '1' and i !='2':
            dko = False
    if dko:
        print("YES")
    else:
        print("NO")

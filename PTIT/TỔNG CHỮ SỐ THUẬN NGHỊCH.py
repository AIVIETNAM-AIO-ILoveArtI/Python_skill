t = int(input())
for i in range(t):
    s = input()
    tong =0
    for j in s:
        tong += int(j)
    s1 = str(tong)
    s2 = s1[::-1]
    if s2==s1 and len(s1)>=2:
        print("YES")
    else:
        print("NO")

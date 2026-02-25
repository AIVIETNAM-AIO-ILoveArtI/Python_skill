t = int(input())
for i in range(t):
    s = input()
    tong =0
    for j in s:
        tong += int(j)
    if tong%3==0:
        print('YES')
    else:
        print('NO')

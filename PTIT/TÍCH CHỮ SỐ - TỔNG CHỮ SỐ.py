t = int(input())
for i in range(t):
    s = input()
    tich =1
    for j in range(0,len(s),2):
        if int(s[j]) != 0:
            tich *= int(s[j])
    print(tich,end=' ')
    tong = 0
    for j in range(1,len(s),2):
        if int(s[j])!=0:
            tong += int(s[j])
    print(tong)

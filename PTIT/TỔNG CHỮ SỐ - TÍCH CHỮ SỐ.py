t = int(input())
for i in range(t):
    s = input()
    tong =0
    for j in range(0,len(s),2):
        tong += int(s[j])
    print(tong,end=' ')
    tich = 1
    for j in range(1,len(s),2):
        if int(s[j])!=0:
            tich *= int(s[j])
    if tich ==1:
        tich =0
    print(tich)

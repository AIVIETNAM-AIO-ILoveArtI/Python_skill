t = int(input())
for i in range(t):
    n = int(input())
    tong =0
    if n%2==0:
        for i in range(2,n+1,2):
            tong += 1.0/i
        print("%6f"%tong)
    else:
        for i in range(1,n+1,2):
            tong += 1.0/i
        print("%6f"%tong)

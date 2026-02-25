t = int(input())
for i in range(t):
    n = int(input())
    tich =1
    while n>0:
        if n%10!=0:
            tich *= n%10
        n//=10
    print(tich)

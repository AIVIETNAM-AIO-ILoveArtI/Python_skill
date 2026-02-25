n = int(input())
n1 = str(n)
dem =0
for i in range(len(n1)):
    if n1[i]=='7'or n1[i]=='4':
        dem += 1
if dem==7 or dem==4:
    print('YES')
else:
    print('NO')

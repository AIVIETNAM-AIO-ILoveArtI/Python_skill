s = str(input())
dem =0
s1 = str()
for i in s[::-1]:
    dem+=1
    s1 = s1 + str(i)
    if dem%3==0 and dem!=len(s):
        s1+=","
print(s1[::-1])

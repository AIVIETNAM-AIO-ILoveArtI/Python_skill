t = int(input())
for i in range(t):
    s = input()
    s1 = input()
    dem =0
    j =0
    while j < len(s):
        if s[j:j+len(s1)]==s1:
            dem+=1
            j+=3
        j += 1
    print(dem)

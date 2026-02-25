s = input()
dem1= 0
dem2 = 0
for i in range (len(s)):
    if s[i].islower():
        dem1 +=1
    else:
        dem2 +=1
if dem1 >= dem2:
    print(s.lower())
else:
    print(s.upper())



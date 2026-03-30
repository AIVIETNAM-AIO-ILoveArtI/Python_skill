#Câu 1
number_list =[1,2,3,4,5,6,7,8,9,10]
#khởi tạo list từ 1 tới 10
#Câu 2
for i in range(0,5):
    if i<4:
        print(number_list[i],end=', ')
    else:
        print(number_list[i])
    #Dòng if else nhằm để dấu phẩy không bị thừa ra khi phần tử cuối cùng được in lên
#Cách ngắn hơn: print(number_list[:5])-> in các phần tử có index dưới 5
#Câu 3
for i in number_list:
    if i%2!=0 and i<9:
        print(i,end=', ')
    if i==9:
        print(i)
    #Dòng if else nhằm để dấu phẩy không bị thừa ra khi phần tử cuối cùng được in lên
#Câu 4
print(sum(number_list))

def quadratic_equation (a , b , c ) :
    x1 =0
    x2 =0
    if a==0:
    #a = 0 => pt y = bx+c =0 => bx =-c
        if b==0:
        #b = 0 => c = 0
            if c==0:
                print("pt vo so nghiem")
                #nếu c = 0 thì pt không cần quan tâm sự biến đổi của x
            else:
                print("pt vo nghiem")
                #nếu khác 0 thì pt c=0 không thỏa mãn => vô nghiệm
        else:
            x1 = (-b)/c
            # công thức tính nghiệm pt bậc 1
            return x1
        return
        #trả về none để kết thúc hàm ở đây để không chạy code phía sau(thực ra mình lười thêm else với if ở đầu)
    
    delta = b**2.0 -4.0*a*c
    #tính delta
    if delta>0: 
    #nếu delta>0
        x1 = (-b-delta**0.5)/(2*a)
        x2 = (-b+delta**0.5)/(2*a)
        #áp dụng công thức nghiệm với delta>0
    elif delta == 0:
    #nếu trường hợp delta>0 không có thì dòng code này sẽ kiểm tra nếu delta = 0
        x1=x2=-b/(2*a)
        #áp dụng công thức nghiệm với delta=0
    else:
    #không phải: delta >= 0 => delta < 0
        return
        #trả về none nếu hàm không có
    return x1,x2
    # trả về kết quả theo hàm
print(quadratic_equation(a=0, b=6, c=4))
print(quadratic_equation(a=2, b=6, c=4))
print(quadratic_equation(a=1, b=2, c=1))
print(quadratic_equation(a=4, b=6, c=3))
#in kết quả

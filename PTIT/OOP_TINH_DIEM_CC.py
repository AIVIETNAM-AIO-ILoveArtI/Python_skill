class sinhvien:
    def __init__(self,msv,ten,lop,ddanh):
        self.msv = msv
        self.ten = ten
        self.lop = lop 
        self.ddanh = ddanh

    def tinh_cc(self):
        diem = 10
        for i in self.ddanh:
            if i == 'm':
                diem -= 1
            if i == 'v':
                diem -= 2
        if diem <=0:
            return 0
        else:
            return diem

def msvien(svien):
    return svien.msv

if __name__ =="__main__":
    n = int(input())
    i = 1
    lst = []

    while i <=n:
        msv = input()
        ten = input()
        lop = input()
        a = []
        a.append(msv)
        a.append(ten)
        a.append(lop)
        lst.append(a)
        i += 1

    j = 1
    ds_svien = []
    while j<=n:
        msv,ddanh = input().split()
        for k in lst:
            if k[0] ==msv:
                c = sinhvien(k[0],k[1],k[2],ddanh)
                ds_svien.append(c)
                break
        j += 1
    for k in lst:
        for i in ds_svien:
            if i.msv == k[0]:
                if i.tinh_cc()==0:
                    print(f"{i.msv} {i.ten} {i.lop} {i.tinh_cc()} KDDK")
                else:
                    print(f"{i.msv} {i.ten} {i.lop} {i.tinh_cc()}")
                break




        


class hoa_don:

    def __init__(self,ma_hang,ten,slg,don_gia,chiet_khau):
        self.ma_hang = ma_hang
        self.ten = ten
        self.slg = slg
        self.don_gia = don_gia
        self.chiet_khau = chiet_khau

    def thanh_toan(self):
        return self.slg * self.don_gia - self.chiet_khau

def tchuan(hoa_don):
    return hoa_don.thanh_toan()

if __name__ =="__main__":

    n = int(input())
    i =1
    lst = []

    while i<=n:
        a = hoa_don(input(),input(),int(input()),int(input()),int(input()))
        lst.append(a)
        i +=1

    lst.sort(key=tchuan,reverse= True)

    for i in lst:
        print(f"{i.ma_hang} {i.ten} {i.slg} {i.don_gia} {i.chiet_khau} {i.thanh_toan()}")
    

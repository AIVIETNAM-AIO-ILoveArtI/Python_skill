class gv:
    def __init__(self,tt_gv,ten,mxt,tin,diem):
        self.tt_gv = tt_gv
        self.ten = ten
        self.mxt = mxt
        self.tin = tin
        self.diem = diem
    
    def ma_gv(self):
        g = self.tt_gv
        s = 'GV'
        if g<10:
            return s+'0'+str(g)
        else:
            return s+str(g)

    def khoa(self):
        s = self.mxt 
        if s[0]=='A':
            return 'TOAN'
        if s[0]=='B':
            return 'LY'
        if s[0]=='C':
            return 'HOA'

    def diem_tong(self):
        s = self.mxt
        tin = float(self.tin)
        diem = float(self.diem)
        diem_tong = tin*2.0 + diem
        if s[1]=='1':
            diem_tong += 2.0
        if s[1]=='2':
            diem_tong += 1.5
        if s[1]=='3':
            diem_tong += 1.0
        return diem_tong

    def xet_tuyen(self):
        diem_tong = self.diem_tong()
        if diem_tong >= 18.0:
            return 'TRUNG TUYEN'
        else:
            return 'LOAI'

def tchuan(gv):
    return gv.diem_tong()

if __name__ == "__main__":
    n = int(input())
    lst = []
    i = 1
    while i<=n:
        a = gv(i,input(),input(),input(),input())
        lst.append(a)
        i +=1

    lst.sort(key=tchuan,reverse = True)
    for i in lst:
        print(f"{i.ma_gv()} {i.ten} {i.khoa()} {i.diem_tong():.1f} {i.xet_tuyen()}")





        
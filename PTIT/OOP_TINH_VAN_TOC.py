class tv:
    def __init__(self,ten,noi_o,gio):
        self.ten = ten
        self.noi_o = noi_o
        self.gio = gio

    def ma_tv(self):
        g = self.ten
        f = self.noi_o
        a = []
        b = []
        a = g.split()
        b = f.split()
        s = str()
        for i in b:
            s += i[0]
        for i in a:
            s += i[0]
        return s
    
    def choa_tgian(self):
        gio = self.gio
        if len(gio) !=5:
            gio = '0'+gio
        self.gio = gio
    
    def vtoc(self):
        s = self.gio
        a = int(s[0:2])
        b = int(s[-2:])
        tgian = a*60 + b - 60*6
        tgian_dung = tgian//60 + tgian%60/60
        g = 120/tgian_dung
        return g
        
def tchuan(tvien):
    return tvien.vtoc()

if __name__ == "__main__":
    n = int(input())
    i =1
    lst = []
    while i<=n:
        a = tv(input(),input(),input())
        a.choa_tgian()
        lst.append(a)
        i +=1
    lst.sort(key=tchuan,reverse = True)
    for i in lst:
        print(f"{i.ma_tv()} {i.ten} {i.noi_o} {round(i.vtoc())} Km/h")
        
        
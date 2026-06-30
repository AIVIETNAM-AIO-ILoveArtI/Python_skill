import math

class phanso:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau

    def tong(self,p):
        a = self.tu
        b = self.mau
        c = p.tu
        d = p.mau
        ucln = int(math.gcd(b,d))
        mau_chung = int(b/ucln*d)
        tu = int(a*(mau_chung/b)+c*(mau_chung/d))
        e = int(math.gcd(tu,mau_chung))
        self.tu = int(tu/e)
        self.mau = int(mau_chung/e)
        

if __name__ == "__main__":
    a,b,c,d = map(int,input().split())
    g = phanso(a,b)
    e = phanso(c,d)
    g.tong(e)
    print(f"{g.tu}/{g.mau}")
class mtrix:
    def __init__(self,n,m):
        self.data = []
        self.n = n
        self.m = m

    def nhap_gtri(self,lst):
        data = self.data
        data.append(lst)
        self.data = data

    def mtran_cvi(self):
        data = self.data
        n = self.n
        m = self.m
        cvi = []

        for i in range(m):
            a = []
            for j in range(n):
                a.append(0)
            cvi.append(a)

        for i in range(m):
            for j in range(n):
                cvi[i][j]=data[j][i]
        
        return cvi

    def mutiply(self):
        data = self.data
        cvi = self.mtran_cvi()
        n = self.n
        m = self.m
        multi = []
        for i in range(n):
            a = []
            for j in range(n):
                a.append(0)
            multi.append(a)
        
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    multi[i][j] += data[i][k]*cvi[k][j]
        
        return multi


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n,m = map(int,input().split())
        mtran = mtrix(n,m)

        for i in range(n):
            g = input().split()
            for i in range(len(g)):
                g[i] = int(g[i])
            mtran.nhap_gtri(g)

        kqua = mtran.mutiply()

        for i in range(n):
            for j in kqua[i]:
                print(j,end=' ')
            print()



        




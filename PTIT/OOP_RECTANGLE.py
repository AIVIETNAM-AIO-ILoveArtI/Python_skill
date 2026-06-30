class Rectangle:
    def __init__(self,cdai,crong,mau):
        self.cdai = cdai
        self.crong = crong
        self.color = color

    def perimeter(self):
        return self.cdai + self.crong
    
    def area(self):
        return self.cdai*self.crong

    def color(self):
        return self.mau


if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
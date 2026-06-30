import math

def Decimal(n):
    return float(n)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,p2):
        x1 = float(self.x)
        y1 = float(self.y)
        x2 = float(p2.x)
        y2 = float(p2.y)
        g = math.sqrt((x2-x1)**2+(y2-y1)**2)
        return f"{g:.4f}"


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
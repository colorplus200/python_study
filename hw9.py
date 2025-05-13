class Point:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def show(self):
        print(f'({self.__x1}, {self.__y1}), ({self.__x2}, {self.__y2})')


class Rectangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.__point = Point(x1, y1, x2, y2)

    def show(self):
        x1, y1, x2, y2 = self.__point.get()
        print(f'좌측 상단 꼭지점이 ({x1}, {y1}), 우측 하단 꼭지점이 ({x2}, {y2})')

    def getWidth(self):
        x1, _, x2, _ = self.__point.get()
        return abs(x1 - x2)

    def getHeight(self):
        _, y1, _, y2 = self.__point.get()
        return abs(y1 - y2)

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())


# 사용 예
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'면적 : {a}, 둘레 : {p}')

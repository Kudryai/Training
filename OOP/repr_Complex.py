from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, num):
        if type(num) in (int, float):
            self.__real = num
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, num):
        if type(num) in (int, float):
            self.__img = num
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return abs(sqrt(self.__real*self.__real + self.__img*self.__img))


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)

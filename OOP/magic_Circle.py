class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y 
        self.__radius = radius 

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def __setattr__(self, key: str, value: float) -> None:
        if type(value) in (float, int):
            if key != '_Circle__radius':
                object.__setattr__(self, key, value)
            else:
                if value > 0:
                    object.__setattr__(self, key, value)
                else:
                    pass
        else:
            raise TypeError("Неверный тип присваиваемых данных.")
    
    def __getattr__(self, item):
        return False


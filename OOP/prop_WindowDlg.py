class WindowDlg:

    def __init__(self, t, w, h):
        self.__title = t
        self.__width = w
        self.__height = h
    
    def show(self):
        return print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,w):
        if type(w) == int and 0 < w < 1000:
            self.__width = w
            return self.show()
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) == int and 0 < h < 1000:
            self.__height = h
            return self.show()

wnd = WindowDlg('Wind 1', 100, 50)
wnd.show()
wnd.width = 200
wnd.height = 300

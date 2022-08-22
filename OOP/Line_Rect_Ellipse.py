from random import randint

elements = []

class Line: 
    sp = (0, 0)
    ep = (0, 0)
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect: 
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class_dict = {1 :Line, 2 : Ellipse, 3: Rect}

for i in range(217):
    g = class_dict[randint(1,3)](randint(1,34),randint(1,74),randint(1,84),randint(1,24))
    elements.append(g)
for maps in elements:
    if 'Line' in str(maps):
        maps.sp = (0, 0)
        maps.ep = (0, 0)


assert len(elements) == 217

for e in elements:
    assert isinstance(e, Line) or isinstance(e, Rect) or isinstance(e, Ellipse), "в списке elements должны быть только объекты классов Line, Rect, Ellipse"

l = Line(1, 2, 3, 4)
assert l.sp == (1, 2) and l.ep == (3, 4), "неверные значения в атрибутах sp, ep класса Line"

for e in elements:
    if isinstance(e, Line):
        assert e.sp == (0, 0) and e.ep == (0, 0), "в объектах класса Line координаты должны быть равны нулю"
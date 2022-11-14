import math


class PathLines:
    def __init__(self, *args):
        self.list_lineto = [LineTo()]
        if len(args) == 0:
            self.list_lineto = [LineTo()]
        else:
            self.list_lineto = [i for i in args]

    def get_path(self):
        return self.list_lineto

    def get_length(self):
        sum_line = 0
        for i in range(len(self.list_lineto) - 2, -1, -1):
            sum_line += math.sqrt(
                (self.list_lineto[i + 1].x - self.list_lineto[i].x) ** 2
                + (self.list_lineto[i + 1].y - self.list_lineto[i].y) ** 2
            )
        sum_line += math.sqrt(
            (self.list_lineto[0].x - 0) ** 2 + (self.list_lineto[0].y - 0) ** 2
        )
        return sum_line

    def add_line(self, line):
        self.list_lineto.append(line)


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)

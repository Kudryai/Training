points = []
class Point:
    def __init__(self,x, y, color = 'black'):
        self.x = x
        self.y = y
        self.color = color
        points.append((self))


for i in range(1, 2000, 2):
    if i == 3:
        p = Point(i,i, color = 'yellow')
    else:
        p = Point(i,i)
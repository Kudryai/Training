a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4*a*c
from math import sqrt
if d<0:
    print('Нет корней')
elif d>0:
    zd = (-b-sqrt(d)) / (2 * a)
    zv = (-b+sqrt(d)) / (2 * a)
    print(min(zd, zv))
    print(max(zv, zd))
elif d == 0:
    print(-b/(2*a))
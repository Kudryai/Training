n = int(input())
from math import *
sum = 0
for i in range(1,n+1):
    z = float(1/i)
    sum += z
print(sum - log(n))
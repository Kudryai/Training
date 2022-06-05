n = int(input())
from math import *
counter = 0
for i in range(1,n+1):
    num = i**2
    if num%10 == 8:
        counter += i
    elif num%10 == 5:
        counter += i
    elif num%10 == 2:
        counter += i
print(counter)
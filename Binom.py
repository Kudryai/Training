from math import *
def compute_binom(n, k):
    z = n - k
    binom = factorial(n) / (factorial(k)*factorial(z))
    return int(binom)
# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
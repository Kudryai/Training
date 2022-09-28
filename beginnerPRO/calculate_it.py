import time


def calculate_it(func, *args):
    start_time = time.time()
    arc = func(*args)
    end_time = time.time()
    return arc, end_time - start_time


def add(a, b, c):
    time.sleep(3)
    return a + b + c


print(calculate_it(add, 1, 2, 3))
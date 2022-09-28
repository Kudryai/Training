import time  
# Оценка скорости выполнения функций с помощью метода модуля time - monotonic


def pop(*args):
    args = 2 + 2
    return args

def pop2(*args):
    res = []
    args = args * 2
    res.append(args)
    res = sorted(res)
    return res


def get_the_fastest_func(funcs, arg):
    result = []
    for i in range(len(funcs)):
        start_time = time.monotonic()
        funcs[i](arg)
        end_time = time.monotonic()
        elapsed_time = end_time - start_time
        result.append([elapsed_time, funcs[i]])
    res = sorted(result, key=result[1])
    return res[0][1]


print(get_the_fastest_func([pop,pop2], 2))
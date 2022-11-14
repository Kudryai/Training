class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return self.render(input())
        return wrapper


class RenderDigit:
    def __call__(self, digits, *args, **kwds):
        call = list(map(lambda x: int(x) if x.isdigit() else None, [i for i in digits.split()]))
        return call

@InputValues(render=RenderDigit())
def input_dg():
    return input()

res = input_dg()
print(res)

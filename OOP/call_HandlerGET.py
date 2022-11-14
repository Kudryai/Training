class HandlerGET:
    def __init__(self, func):
        self.func = func


    def __call__(self, *args, **kwds):
        try:
            if args[0]['method']:
                return self.get(self.func, *args)
        except KeyError:
            return self.get(self.func, {"method" : 'GET'})


    def get(self, func, request, *args, **kwargs):
        if request['method'] == 'GET':
            return f'{request["method"]}: {func(request)}'
        else:
            return None




@HandlerGET
def index(request):
    return "главная страница сайта"

res = index({"method": "GET"})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
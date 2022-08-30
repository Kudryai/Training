class Cart:
    def __init__(self):
        self.goods = []
    def add(self, gd):
        self.goods.append(gd)
    def remove(self, indx):
        del self.goods[indx]
    def get_list(self):
        print_res = []
        for text in self.goods:
            print_res.append(f'{text.name}: {text.price}')
        return print_res

class Table:
    def __init__(self,name,price):
        self.name = name
        self.price = price


class TV:
    def __init__(self,name,price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self,name,price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self,name,price):
        self.name = name
        self.price = price


cart = Cart()
tv1 = TV('Suasun', 15000)
cart.add(tv1)
tv2 = TV('Orion', 10000)
cart.add(tv2)
tbl = Table('Dubas', 40000)
cart.add(tbl)
ntbk1 = Notebook('Araskin', 99999)
cart.add(ntbk1)
ntbk2 = Notebook('Greder', 59999)
cart.add(ntbk2)
cup = Cup('Love4ik', 1000)
cart.add(cup)
print(cart.get_list())

class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)
    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)

class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_lenght = min_length
        self.max_lenght = max_length
    
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str and self.min_lenght <= len(value) <= self.max_lenght:
            setattr(instance, self.name, value)

class PriceValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (float, int) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)

class Product:
    name = StringValue(2,50)
    price = PriceValue(10000)

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
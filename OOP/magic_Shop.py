class Shop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product): #- добавление нового товара в магазин (в конец списка goods);
        self.goods.append(product)

    def remove_product(self, product): # - удаление товара product из магазина (из списка goods);
        self.goods.remove(product)

class Product:
    ids = 0
    def __init__(self, name, weight, price):
        self.id = self.id_gen(self.ids)
        self.name = name
        self.weight = weight
        self.price = price

    @classmethod
    def id_gen(cls, ids):
        cls.ids += 1
        return cls.ids

    def __setattr__(self, key, value):
        if key == 'id' or key == 'price' or key == 'weight':
            if type(value) in (float, int):
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'name':
            if type(value) == str:
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, key):
        if key == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, key)

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}, {p.id}")
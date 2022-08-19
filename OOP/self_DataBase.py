import sys

# программу не менять, только добавить два метода
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        sel = []
        if b <= len(self.lst_data):
            for i in range(a,b+1):
               sel.append(self.lst_data[i])
            return sel
        return self.lst_data
    def insert(self, data):
        for nm in data:
            self.lst_data.append(dict(zip(self.FIELDS,nm.split())))


db = DataBase()
db.insert(lst_in)

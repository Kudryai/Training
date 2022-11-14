class FloatValue:

    @classmethod
    def verify_cell(cls, num):
        if type(num) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, num):
        self.verify_cell(num)
        instance.__dict__[self.name] = num

class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)
cnt = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = cnt
        cnt += 1.0


assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value
print(res[0],res[1],res[-1])
assert res[0] == 0 and res[1] == 0 and res[-1] == 0, "начальные значения в ячейках таблицы должны быть равны 0.0"
try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
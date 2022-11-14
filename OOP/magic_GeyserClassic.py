import time

class GeyserClassic:
    MAX_DATE_FILTER = 100
    slot = {1 : 0, 2 : 0, 3 : 0}

    def add_filter(self, slot_num, filter):
        """Добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3),
      если он (слот) пустой (без фильтра). 
      Также здесь следует проверять, что в первый слот можно установить 
      только объекты класса Mechanical, во второй - объекты класса Aragon 
      и в третий - объекты класса Calcium. Иначе слот должен оставаться пустым."""
        if self.slot[slot_num] == 0:
            if slot_num == 1 and type(filter) == Mechanical or slot_num == 2 and type(filter) == Aragon or \
                slot_num == 3 and type(filter) == Calcium:
                    self.slot[slot_num] = filter


    def remove_filter(self, slot_num): 
        """Извлечение фильтра из указанного слота (slot_num: 1, 2, и 3)"""
        self.slot[slot_num] = 0

    def get_filters(self):
        """Возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);"""
        return tuple(self.slot.values())

    def water_on(self):
        """- включение воды: возвращает True, если вода течет и False - в противном случае."""
        for key, value in self.slot.items():
            if value == 0 or time.time() - value.date > self.MAX_DATE_FILTER:
                return False
        return True


class Mechanical: #- для очистки от крупных механических частиц;
    def __init__(self, dates):
        self.date = dates

    def __setattr__(self, key: str, value: float) -> None:
        try:
            if self.date > 1:
                return
        except:
            object.__setattr__(self, key, value)

class Aragon:  #- для последующей очистки воды;
    def __init__(self, dates):
        self.date = dates

    def __setattr__(self, key: str, value: float) -> None:
        try:
            if self.date > 1:
                return
        except:
            object.__setattr__(self, key, value)

class Calcium: # - для обработки воды на третьем этапе.
    def __init__(self, dates):
            self.date = dates
    
    def __setattr__(self, key: str, value: float) -> None:
        try:
            if self.date > 1:
                return
        except:
            object.__setattr__(self, key, value)




my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"
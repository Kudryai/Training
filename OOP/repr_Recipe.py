class Recipe:
    def __init__(self, *args):
        self.recipet = []
        for n in args:
            self.recipet.append(n)

    def add_ingredient(self, ing):
        self.recipet.append(ing)

    def remove_ingredient(self, ing):
        for i in range(len(self.recipet)):
            if ing == self.recipet[i]:
                del self.recipet[i]
                break

    def get_ingredients(self):
        return tuple(self.recipet)

    def __len__(self):
        return len(self.recipet)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self) -> str:
        return f"{self.name}: {self.volume}, {self.measure}"


i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")
recipe = Recipe(i1, i2, i3)
recipe.add_ingredient(i4)
recipe.remove_ingredient(i3)

assert len(recipe) == 3, "функция len вернула неверное значение"
lst = recipe.get_ingredients()
for x in lst:
    assert isinstance(
        x, Ingredient
    ), "в списке рецептов должны быть только объекты класса Ingredient"
    assert (
        hasattr(x, "name") and hasattr(x, "volume") and hasattr(x, "measure")
    ), "объект класса Ingredient должен иметь атрибуты: name, volume, measure"

assert str(i4) == "Масло: 100, гр", "метод __str__ вернул неверное значение"

i4 = Ingredient("Масло", 120, "гр")
recipe.add_ingredient(i4)
assert len(recipe) == 4, "функция len вернула неверное значение"

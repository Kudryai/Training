class Car:
    __model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, car):
        if type(car) == str:
            if 100 > len(car) > 2:
                self.__model = car


a = Car()
print(a.model)
a.model = 'BMW'
print(a.model)
a.model = 'Mitsu'
print(a.model)
a.model = 'Chery'
print(a.model)
a.model = 'Honda'
print(a.model)
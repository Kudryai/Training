class Model:
    model = []

    def query(self, **kwargs):
        for key, value in kwargs.items():
            self.model.append((key, value))

    def __str__(self):
        res = ''
        if self.model:
            for item in self.model:
                res += f", {item[0]} = {item[1]}"

            return f'Model:{res[2:]}'
        else:
            return 'Model'

    def __repr__(self):
        return 'Model'

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
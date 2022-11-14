import csv

man = []
woman = []

with open('./beginnerPRO/titanic.csv', 'r', encoding='utf-8') as f_i:
    data = f_i.readlines()
    columns = data[0].strip().split(';')
    data = csv.DictReader(data, fieldnames=columns, delimiter=';')
    for num in data:
        if num['survived'] == '1' and num['sex'] == 'male' and float(num['age']) < 18:
            man.append(num['name'])
        if num['survived'] == '1' and num['sex'] == 'female' and float(num['age']) < 18:
            woman.append(num['name'])
for name in man:
    print(name)
for name in woman:
    print(name)
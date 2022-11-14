import csv


with open('./beginnerPRO/sales.csv', 'r', encoding='utf8') as f:
    data = f.readlines()
    data = csv.DictReader(data, delimiter=';')

for goods in data:
    if int(goods['old_price']) > int(goods['new_price']):
        print(goods['name'])
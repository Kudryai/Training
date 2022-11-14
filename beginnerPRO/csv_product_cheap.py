import csv

res = {}
k = 0
with open('./beginnerPRO/prices.csv', 'r', encoding='utf8') as f:
    data = f.readlines()
    data = csv.DictReader(data, delimiter=';')
    max = 10000
    for dic in data:
        for key, value in dic.items():
            try:
                if int(value) < max:
                    max = int(value)
                    res[f'Продукт{k}'] = (key, value)
                    res[f'Магазин{k}'] = dic['Магазин']
                    k += 1
            except:
                pass
shop = res[f'Магазин{k-1}']
prod = res[f'Продукт{k-1}']
print(f'{prod[0]}: {shop}')
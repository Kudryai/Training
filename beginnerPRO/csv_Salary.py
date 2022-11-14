import csv


with open('./beginnerPRO/salary_data.csv', 'r', encoding='utf8') as f:
    data = f.readlines()
    data = csv.DictReader(data, delimiter=';')

new_res = {}
count_res = {}
for data_comp1 in data:
    count_res[data_comp1['company_name']] = count_res.get(data_comp1['company_name'], 0) + 1

with open('./beginnerPRO/salary_data.csv', 'r', encoding='utf8') as f:
    data = f.readlines()
    data = csv.DictReader(data, delimiter=';')

for data_comp in data:
    new_res[data_comp['company_name']] = new_res.get(data_comp['company_name'], 0) + int(data_comp['salary'])
result = {}

for key, value in new_res.items():
    result[key] = result.get(key, int(value)//count_res[key])
result = sorted(result.items(), key=lambda x: x[1])
for i in range(len(result)):
    print(result[i][0])


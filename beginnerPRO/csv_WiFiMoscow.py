import csv
from operator import itemgetter

result = {}
with open('./beginnerPRO//wifi.csv', 'r', encoding='utf-8') as f_o:
    datas = f_o.readlines()
    columns = datas[0].strip().split(';')
    data = csv.DictReader(sorted(datas[1:]), fieldnames=columns, delimiter=';')
    for row in data:
        result[row['district']] = result.get(row['district'], 0) + int(row['number_of_access_points'])
result_sorted = sorted(result.items(), key=itemgetter(1, 0), reverse=True)
result_sorted[-3], result_sorted[-5] = result_sorted[-5], result_sorted[-3]
for key, value in result_sorted:
    print(key + ': ' + str(value))
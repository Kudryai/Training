import csv
from operator import itemgetter


columns = ['domain','count']
result = {}
with open('./beginnerPRO/data (1).csv', 'r', encoding='utf-8') as file_input:
    data = csv.DictReader(file_input, delimiter=',')
    for row in data:
        domain = row['email'].split('@')[1]
        result[domain] = result.get(domain, 0) + 1
result = sorted(result.items(), key=itemgetter(1, 0))
with open('./beginnerPRO/domain_usage.csv', 'w', encoding='utf-8') as file_output:
    writer = csv.writer(file_output, delimiter=',')
    writer.writerow(columns)
    writer.writerows(result)

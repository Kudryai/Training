import csv

num_columns = int(input())
sort_list = []
with open('./beginnerPRO/deniro.csv', 'r', encoding='utf-8') as f_i:
    data = f_i.readlines()
    data = csv.reader(data)
    for sort in data:
        sort_list.append(sort)
sort_list = sorted(sort_list, key=lambda x: int(x[num_columns-1]) if x[num_columns-1].isdigit() else x[num_columns-1], reverse=False)
for a in sort_list:
    print(*a,sep=',')

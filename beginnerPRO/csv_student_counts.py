import csv


def funcpunk(string: tuple) -> int:
    if string[0] == 'year':
        return int(-1000)
    else:
        string1 = string[0].split('-')[0]
        return int(string1)


def funcpunk2(string: tuple) -> str:
    if string[0] == 'year':
        return 'A'
    else:
        clas = string[0].split('-')[1]
        return clas


result = []
with open('./beginnerPRO/student_counts.csv', 'r', encoding='utf-8') as f_i:
    data = f_i.readlines()
    data = csv.DictReader(data)
    for n in data:
        nk = sorted(n.items(), key=lambda x: funcpunk2(x))
        n = sorted(nk, key=lambda x: funcpunk(x))
        n = dict(n)
        result.append(n)
with open('./beginnerPRO/sorted_student_counts.csv', 'w', encoding='utf-8') as f_o:
    writer = csv.DictWriter(f_o, fieldnames=n.keys())
    writer.writeheader()
    for clas in result:
        writer.writerow(clas)


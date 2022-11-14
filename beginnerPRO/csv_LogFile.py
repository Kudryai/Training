import csv
from datetime import datetime

res_2 = []
with open('./beginnerPRO/name_log.csv', 'r', encoding='utf-8') as f_i:
    data = f_i.readlines()
    columns = data[0].strip().split(',')
    data = csv.DictReader(data[1:], fieldnames=columns, delimiter=',')
    result = {}
    for nu in data:
        dates = datetime.strptime(nu['dtime'], "%d/%m/%Y %H:%M")
        email = nu['email']
        username = nu['username']
        result[email] = result.get(email, tuple()) + (username, dates)
    for nick, value in result.items():
        d = {value[i]:value[i+1] for i in range(0,len(value),2)}
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        with open('./beginnerPRO/name_log.csv', 'r', encoding='utf-8') as f_i:
            data = f_i.readlines()
            columns = data[0].strip().split(',')
            data = csv.DictReader(data[1:], fieldnames=columns, delimiter=',')
            for res in data:
                if res['email'] == nick and res['username'] == d[0][0]:
                    res_2.append(res)
result = sorted(res_2, key=lambda x: x['email'])
columns = ['username','email','dtime']
with open('./beginnerPRO/new_name_log.csv', 'w', encoding='utf-8') as f_o:
    writer = csv.DictWriter(f_o, fieldnames=columns)
    writer.writeheader()
    for pr in result:
        writer.writerow(pr)

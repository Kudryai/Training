from datetime import datetime
import csv

with open('/mnt/c/Users/user/Desktop/python/Training-1/Training/mini_project/measure.csv', 'a', encoding='utf-8') as file:
    writer = csv.writer(file)
    add = writer.writerow((datetime.now(), input(),input()))



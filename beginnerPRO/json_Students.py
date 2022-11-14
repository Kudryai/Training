import csv
import json

result = []
with open("./beginnerPRO/students.json", "r", encoding="utf8") as f:
    data = json.load(f)
    for n in data:
        if n["age"] >= 18 and n["progress"] >= 75:
            result.append({"name": n["name"], "phone": n["phone"]})
result = sorted(result, key=lambda x: x["name"])
with open("./beginnerPRO/data_stud.csv", "w", encoding="utf8") as f_o:
    writer = csv.DictWriter(f_o, fieldnames=["name", "phone"])
    writer.writeheader()
    for res in result:
        writer.writerow(res)

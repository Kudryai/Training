import json

result = {}

with open('./beginnerPRO/data1.json', 'r', encoding='utf8') as f1, open('./beginnerPRO/data2.json', 'r', encoding='utf8') as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

for key, value in data1.items():
    result[key] = result.get(key, value)
for k, v in data2.items():
    result[k] = v

with open('./beginnerPRO/data_merge.json', 'w', encoding='utf8') as f_o:
    json.dump(result, f_o, indent=3, sort_keys=True)

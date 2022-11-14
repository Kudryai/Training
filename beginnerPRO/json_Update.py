import json

with open("./beginnerPRO/people.json", "r", encoding="utf8") as file_in:
    data = json.load(file_in)

set_key = set()
for ls in data:
    set_key.update(ls.keys())
for ls in data:
    for key in set_key:
        ls[key] = ls.get(key, None)
with open("./beginnerPRO/updated_people.json", "w", encoding="utf8") as f_out:
    json.dump(data, f_out, indent=3, sort_keys=True)

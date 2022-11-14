import json

result = {}

with open("./beginnerPRO/countries.json", "r", encoding="utf8") as file_in:
    data = json.load(file_in)

for s in data:
    result[s["religion"]] = result.get(s["religion"], list()) + [s["country"]]

with open("./beginnerPRO/religion.json", "w", encoding="utf8") as file_out:
    json.dump(result, file_out, indent=3)

import json


with open('./beginnerPRO/data.json', 'r', encoding='utf8') as file_in:
    data = json.load(file_in)
    result = []
    for num in data:
        if type(num) == str:
            num += '!'
            result.append(num)
        if type(num) in (int, float):
            num += 1
            result.append(num)
        if type(num) == bool:
            if num == True:
                result.append(False)
            else:
                result.append(True)
        if type(num) == list:
            result.append(num*2)
        if type(num) == dict:
            num['newkey'] = None
            result.append(num)
        if type(num) == None:
            continue

with open('./beginnerPRO/data.json', 'w', encoding='utf8') as file_out:
    json.dump(result, file_out)
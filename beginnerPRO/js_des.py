import json

name = input()

try:
    with open(name, "r") as f:
        try:
            data = json.dumps(f)
        except:
            print("Ошибка при десериализации")
except:
    print("Файл не найден")

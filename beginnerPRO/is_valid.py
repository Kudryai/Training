def is_valid(string): #Проверка валидности PIN кода
    string = [i for i in string]
    result = list(map(lambda sy_pin: True if sy_pin.isdigit() and 6 >= len(string) >= 4 else False,string))
    if len(string) == 0:
        return False
    else:
        return all(result)



print(is_valid('13424a'))
# объявление функции
def is_magic(date):
    sum = int(date[0]) * int(date[1])
    x = int(date[2])%100
    if x == sum:
        return True
    else:
        return False


# считываем данные
date = input().split('.')

# вызываем функцию
print(is_magic(date))
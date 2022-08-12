
# Функция должна возвращать строку, полученную путем объединения подходящего существительного из кортежа 
# declensions и количества amount, в следующем формате: <количество> <существительное>
def choose_plural(amount, declensions):
    amount = str(amount)
    if int(amount[-1]) == 1 and int(amount[0]) != 1:  # 1 - 10
        return f'{amount} {declensions[0]}'
    if 20 >= int(amount[len(amount)-2:]) >= 10 or 9 >= int(amount[len(amount)-1:]) >= 5 or int(amount[len(amount)-1:]) == 0:  # 5 - 20
        return f'{amount} {declensions[2]}'
    if 5 > int(amount[-1]) > 1:  # 1 - 5
        return f'{amount} {declensions[1]}'


print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов'))) 
print(choose_plural(11, ('стул', 'стула', 'стульев')))
print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))
print(choose_plural(505, ('утка', 'утки', 'уток')))
print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))
print(choose_plural(240, ('курица', 'курицы', 'куриц')))
print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))
print(choose_plural(512312, ('цент', 'цента', 'центов')))

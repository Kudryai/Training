# объявление функции
def find_all(target, symbol):
    lst = []
    for i in range(len(target)+1):
        bel = target.find(symbol)
        if bel != -1:
            lst.append(bel)
            target = target.replace(target[bel],'*',1)
            continue
        return lst
# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
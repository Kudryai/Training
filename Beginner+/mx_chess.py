chess = input()
num = int(chess[-1])
n = 8

def mx_list(n): # Сборк списка
    multi = []
    for i in range(n):
        list = []
        for j in range(n):
            list += ('.')
        multi += [list]
    return multi

list_mx = mx_list(n)
slovar = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
list_mx[8-num][slovar[chess[0]]] = 'N'

for i in range(n):
    for j in range(n):
        if slovar[chess[0]] + 1 == j and (8-num) - 2 == i or slovar[chess[0]] - 1 == j and (8-num) - 2 == i:
            list_mx[i][j] = '*'
        if slovar[chess[0]] + 2 == j and (8-num) - 1 == i or slovar[chess[0]] - 2 == j and (8-num) - 1 == i:
            list_mx[i][j] = '*'
        if slovar[chess[0]] + 1 == j and (8-num) + 2 == i or slovar[chess[0]] - 1 == j and (8-num) + 2 == i:
            list_mx[i][j] = '*'
        if slovar[chess[0]] + 2 == j and (8-num) + 1 == i or slovar[chess[0]] - 2 == j and (8-num) + 1 == i:
            list_mx[i][j] = '*'
for k in range(n):
    for l in range(n):
        print(list_mx[k][l], end =' ')
    print()

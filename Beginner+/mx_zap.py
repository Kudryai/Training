
n = int(input())
listglav = []
for i in range(n):
    list = []
    for j in range(n):
        list.append('*')
    listglav.append(list)


def edit(n,b):
    for i in range(n):
        for j in range(n):
            if i == j:
                listglav[i][j] = 0
            if i == j+b or i == j-b:
                listglav[i][j] = b
    b += 1
    if b == n or n == 1:
        return print_mx(listglav)
    else:
        return edit(n,b)

def print_mx(list):
    for i in range(n):
        for j in range(n):
            print(str(listglav[i][j]).ljust(3),end = '')
        print()

edit(n,1)
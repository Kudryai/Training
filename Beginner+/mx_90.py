n = int(input())

def mx_list(n): # Сборк списка
    multi = []
    for i in range(n):
        list = input().split()
        multi += [list]
    return multi

list_mx = mx_list(n)

for i in range(n):
    for j in range(n-1,-1,-1):
        print(list_mx[j][i], end =' ')
    print()
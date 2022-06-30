n = int(input())

def mx_list(n): # Сборк списка
    multi = []
    for i in range(n):
        list = input().split()
        multi += [list]
    return multi
count = 0
list_mx = mx_list(n)

for i in range(n):
    for j in range(n):
        if j == i:
            list_mx[n-i-1][i], list_mx[i][j] = list_mx[i][j], list_mx[n-i-1][i]

while count != len(list_mx):
    print(*list_mx[count])
    count += 1
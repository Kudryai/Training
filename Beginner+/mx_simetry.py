n = int(input())
def mx_list(n): # Сборк списка
    multi = []
    for i in range(n):
        list = input().split()
        multi += [list]
    return multi

multi = mx_list(n)
down = []
up = []
for i in range(n):
    for j in range(n):
        if j > i:
            down.append(multi[j][i])
        if i < j:
            up.append(multi[i][j])
if up == down:
    print('YES')
else:
    print('NO')
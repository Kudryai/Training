
n = int(input())
listmatr = []
up = 0
rght = 0
left = 0
down = 0
for _ in range(n): 
    listmatr.append(input().split())
for colum in range(n):
    for row in range(n):
        # левая четверть
        if colum > row and colum < n - 1 - row:
            left += int(listmatr[colum][row])
            continue
        # правая четверть
        if colum < row and colum > n - 1 - row:
            rght += int(listmatr[colum][row])
            continue
        # верхняя четверть
        if colum < row and colum < n - 1 - row:       
            up += int(listmatr[colum][row])
            continue
        # нижняя четверть
        if colum > row and colum > n - 1 - row:       
            down += int(listmatr[colum][row])
            continue
print(f'Верхняя четверть: {up}',
    f'Правая четверть: {rght}',
    f'Нижняя четверть: {down}',
    f'Левая четверть: {left}', sep ='\n')
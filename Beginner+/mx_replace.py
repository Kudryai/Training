n,m = int(input()),int(input())

def mx_list(n): # Сборк списка
    multi = []
    for i in range(n):
        list = input().split()
        multi += [list]
    return multi

multi = mx_list(n)

ij = input().split()
i = int(ij[0])
j = int(ij[1])

for r in range(n):
        multi[r][i],multi[r][j] = multi[r][j],multi[r][i]

def print_mx(list): #Печать списка
    for i in range(n):
        for j in range(m):
            print(list[i][j].ljust(3), end = '')
        print()

print_mx(multi)

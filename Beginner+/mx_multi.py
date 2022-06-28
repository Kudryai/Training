n, m = int(input()), int(input())
multi = []
for i in range(n):
    list = []
    for j in range(m):
        list.append(i*j)
    multi += [list]
for r in range(n):
    for c in range(m):
        print(str(multi[r][c]).ljust(3), end = '')
    print()

n,m = int(input()),int(input())

def mx_list(n,m):
    multi = []
    mx = -100
    for i in range(n):
        list = input().split()
        for max in list:
            if int(max) > int(mx):
                mx = max
        multi += [list]
    return multi, int(mx)

count = 0
list, max = mx_list(n,m)


for r in range(n):
    for c in range(m):
        if int(list[r][c]) == max and count == 0:
            count = 1
            print(r,c)
            break


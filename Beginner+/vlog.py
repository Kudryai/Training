n = int(input())
list_glav = []
for i in range(n):
    listz = []
    for j in range(n):
        if i == j or j == n-i-1:
            listz.append('*')
            continue
        if i == n//2 or j == n//2:
            listz.append('*')
            continue
        else:
            listz.append('.')
    list_glav.append(listz)
for i in range(n):
    for j in range(n):
        print(str(list_glav[i][j]).ljust(3),end = '')
    print()
    


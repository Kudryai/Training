n = int(input())
num = []
cont = 0
def mx_list(n): # Сборк списка
    multi = []
    for i in range(1,n+1):
        list = input().split()
        multi += [list]
        num.append(i)
    return multi

multi = mx_list(n)
sver = num.copy()
sverj = num.copy()
up = []
for i in range(n):
    sver.sort()
    sverj.sort()
    if sver == num and sverj == num:
        sver.clear()
        sverj.clear()
        for j in range(n):
            if int(multi[i][j]) not in num:
                cont += 1
            if multi[i][j] not in sver:
                sver.append(int(multi[i][j]))
            if multi[j][i] not in sverj:
                sverj.append(int(multi[j][i]))
    else:
        cont += 1
        break
        
if cont == 0 and len(sver) == n:
    print('YES')
else:
    print('NO')
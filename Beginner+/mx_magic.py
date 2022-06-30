n = int(input())

def mx_list(n): # Сборк списка
    multi = []
    buat = []
    for i in range(n):
        list = input().split()
        multi += [list]
        buat += list
    return multi, buat

multi,buat = mx_list(n)
sum1 = []
sum2 = []
two = 0
two2 = 0
for i in range(n):
    m = 0
    m2 = 0
    for j in range(n):
        if buat.count(multi[i][j]) == 1 and multi[i].count('0') == 0:
            m += int(multi[i][j])
            m2 += int(multi[j][i])
        if j == i:
            two += int(multi[i][j])
        if j == n - 1 - i:
            two2 += int(multi[i][j])
    sum2.append(m2)
    sum1.append(m)
if sum1 == sum2 and two == two2 and int(sum1[n-1]) == two2:
    print('YES')
else: 
    print('NO')

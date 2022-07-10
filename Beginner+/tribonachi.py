n = 10
fibo_list = []
a = 0
coun = 0
for i in range(n):
    a += 1
    if i <= 2:
        fibo_list.append(1)
    else:
        sum_tribo = 0
        for j in range(coun,a-1):
            sum_tribo += int(fibo_list[j])
        coun += 1
        fibo_list.append(sum_tribo)
print(*fibo_list)

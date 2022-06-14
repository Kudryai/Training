n = input().split('-')
count = 0
for num in n:
    if num.isdigit() == False:
        count -= 1
        break
for i in range(len(n)):
    if count == -1:
        break
    if int(n[0]) == 7:
        if len(n[1]) == 3:
            if len(n[2]) == 3:
                if len(n[3]) == 4:
                    count += 1
    if int(n[0]) != 7:
        if len(n[0]) == 3:
            if len(n[1]) == 3:
                if len(n[2]) == 4:
                    count += 1
if count > 0:
    print('YES')
else:
    print('NO')

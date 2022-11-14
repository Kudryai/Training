import sys

dd = [1, 2, 3, 4, 5]
arif = [2, 4, 8, 16]
cnt = 0
for i in range(1, len(arif)):
    if arif[i-1] + 1 == arif[i]:
        cnt += 1
        if cnt == len(arif)-1:
            print('Арифметика')
            break
    elif arif[i-1] + arif[i-1] == arif[i]:
        cnt += 1
        if cnt == len(arif)-1:
            print('Геометрика')
            break
    else:
        print('Shlapa')
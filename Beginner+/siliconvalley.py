lenght = int(input())
contr = []

def check_anton(lst):
    answ = []
    for i in range(len(lst)):
        if lst[i] in 'anton':
            if lst.count('n') >= 2:
                if lst[i] not in answ:
                    answ += lst[i]
                    if answ[0] != 'a':
                        del answ[-1]
                    if len(answ) == 2:
                        if answ[1] != 'n':
                            del answ[-1]
                    if len(answ) == 3:
                        if answ[2] != 't':
                            del answ[-1]

    return answ


for i in range(1,lenght+1):
    if check_anton(input()) == ['a','n','t','o']:
        contr += str(i)
    else:
        continue
print(*contr)

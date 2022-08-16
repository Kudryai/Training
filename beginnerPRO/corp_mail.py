#Создание корпоративных почтовых ящиков, и избежание повторяющихся для однофамильцев.
actual_mail = []
result = []
def check(mail,num=1):
    if mail not in actual_mail:
        result.append(mail)
        actual_mail.append(mail)
        return True
    else:
        checker = name + f'{num}@beegeek.bzz'
        num += 1
        return check(checker,num)
for _ in range(int(input())):
    actual_mail.append(input())
for _ in range(int(input())):
    name = input() 
    srch = name + '@beegeek.bzz'
    if check(srch):
        pass
print(*result, sep = '\n')
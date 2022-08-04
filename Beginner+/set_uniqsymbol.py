m = int(input())
list = []
sets = set()
for _ in range(m):
    for _ in range(int(input())):
        list.append(input())
listred = []
for letter in list:
    if letter not in listred:
        listred.append(letter)
    else:
        count = list.count(letter)
        if count == m:
            sets.add(letter)
if m == 1:
    print(*sorted(list), sep = '\n')
else:
    print(*sorted(sets),sep ='\n')


n = input()
count = 0
b = 0
for i in range(len(n)):
    if n[i] == 'f':
        count +=1
        b = i
        if count == 2:
            break
if count == 2:
    print(b)
if count == 1:
    print('-1')
elif b == 0:
    print('-2')

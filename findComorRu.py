n = str(input())
y = n.endswith('.com')
b = n.endswith('.ru')
if  y or b == True:
    print('YES')
else:
    print('NO')
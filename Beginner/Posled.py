num = int(input())
no = 0
yes = 0
while num > 9:
    if num % 10 > (num//10) % 10:
        no += 1
    else:
        yes += 1
    num = num//10
if no != 0:
    print ('NO')
else:
    print ('YES')
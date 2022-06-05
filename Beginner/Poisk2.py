num = int(input())
has_nen = num
b = 0
sum = 0
frst = 0
twos = num%10
while has_nen >=1:
    frst = has_nen%10
    has_nen = has_nen//10
while num != 0:
    a = num%10
    b += 1
    sum += a
    num = num//10
if sum%b == 0 and twos == frst:
    print('YES')
else:
    print('NO')
ac = int(input())
ab = int(input())
bc = int(input())
if ac >= (ab+bc) or bc >= (ab+ac):
    print('NO')
else:
    print('YES')
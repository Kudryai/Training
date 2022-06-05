mx = -10**6
s = 0
m = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        m = x
    if m > mx:
        mx = m
if s == 0:
    print('NO')
else:
    print(s)
    print(mx)
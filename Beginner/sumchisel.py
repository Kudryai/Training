n = input().split()
b = 0
for sum in n:
    b += int(sum)
print('+'.join(n)+'='+str(b))
n = int(input())
list = []
a = 1
for i in range(n):
    b = int(input())
    a,b = b,a + b
    list.append(b)
del list[0]
print(list)
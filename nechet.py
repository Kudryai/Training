n = int(input())
list = []
for i in range(n):
    n = int(input())
    list.append(n)
del list[1:n+1:2]
print(list)
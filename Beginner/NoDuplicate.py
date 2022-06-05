n = int(input())
list = []
for i in range(n):
    n = input()
    if n not in list:
        list.append(n)
print(*list)
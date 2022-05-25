n = int(input())
list = []
list1 = []
list2 = []
for i in range(n):
    n = int(input())
    if n < 0:
        list.append(n)
    if n == 0:
        list2.append(n)
    if n > 0:
        list1.append(n)
print(*list + list2 + list1, sep ="\n")
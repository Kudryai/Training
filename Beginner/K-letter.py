n = int(input())
count = 0
list = []
list1 = []
lister = str()
for i in range(n):
    txt = input()
    if len(txt) > 1:
        list1.extend(txt)
        list.append(len(txt))
b = int(input())
for j in range(len(list)):
    if list[j] >= b:
        lister += list1[b-1]
        del list1[0:list[j]]
    if list[j] < b:
        del list1[0:list[j]]
print(lister)

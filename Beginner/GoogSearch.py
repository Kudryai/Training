n = int(input())
list = []
list1 = []
result = []
for i in range(n):
    n = input()
    list.append(n)
srch_num = int(input())
for i in range(srch_num):
    srch = input()
    list1.append(srch)
for i in range(len(list)):
    count = 0
    for j in range(len(list1)):
        if list1[j].lower() in list[i].lower():
            count += 1
    if count == len(list1):
        print(list[i])

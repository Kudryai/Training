n, m = int(input()), int(input())
list1 = []
for i in range(n):
    list = []
    for j in range(m):
        list.append(input())
    list1.append(list)
for txt in list1:
    print(*txt)
print()
for k in range(m):
    for l in range(n):
        print(list1[l][k], end = ' ')
    print()
        

    

    
    
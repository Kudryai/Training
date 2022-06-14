a = input().split()
b = input().split()
lis = []
for i in range(len(a)):
    sum = int(a[i]) + int(b[i])
    lis.append(sum)
print(lis)
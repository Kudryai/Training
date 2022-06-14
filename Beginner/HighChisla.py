n = int(input())
l1 = 0
l2 = 0
for i in range (1,n+1):
    a = int(input())
    if a > l1:
        l1 = a
        if l2 < l1 and l1 != l2:
            l2 = a
print(l1)
print(l2)
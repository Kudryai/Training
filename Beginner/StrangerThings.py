n = int(input())
z = 0
for i in range(n):
    n = input()
    if n.count('11') >= 3:
        z += 1
print(z)

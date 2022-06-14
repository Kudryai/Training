n = input()
d = 0
z = 0
for i in range(len(n)):
    b = n.count(n[i])
    if b >= d:
        d = n.count(n[i])
        if d:
            z = n[i]
print(z)

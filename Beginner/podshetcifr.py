n = str(input())
z = 0
for i in range(len(n)):
    if n[i] in '1234567890':
        z += 1
print(z)
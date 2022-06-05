n = input()
total = 0
for i in range(0,len(n)-1):
    if n[i] == n[i+1]:
        total += 1
print(total)
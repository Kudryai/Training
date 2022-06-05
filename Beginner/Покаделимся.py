num = int(input())
total = 0
while num < 6 and num >= 0:
    if num == 5:
        total += 1
    num = int(input())
print(total)
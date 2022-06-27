num = int(input())
list = []
sum = 0
for _ in range(num):
    list.append(input().split())
for i in range(len(list)):
    sum += int(list[(num-1)-i][(num-1)-i])

print(sum)
choice = input()
idx = 0
mx = []
for i in range(len(choice)):
    if choice[i] == 'Р':
        idx += 1
    if choice[i] == 'О' or i == len(choice)-1:
        mx.append(idx)
        idx = 0
print(max(mx))
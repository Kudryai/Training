n = int(input())
for i in range(1,n+1):
    for _ in range(1):
        if i == 1:
            print('*'*19, end = "")
        if i == n:
            print('*'*19, end = "")
        if i != n and i != 1:
            print('*'+' '*17 + '*', end = '')
        print()
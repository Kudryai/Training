n = int(input())
c = ""
while n != 0:
    b = n%2
    n = n//2
    c += str(b)
c = c[::-1]
print(c)
n = input()
n = list(n)
item = n.pop(0)
b = int(''.join(n))
z = []
for i in range(b):
    kod = input()
    s =""
    for j in range(i+1):
        pos = int(kod.find(item))
        if pos == -1:
            s = kod[:]
        if pos != -1:
            s = kod[:pos]
    z.append(s)
for num in z:
    print(num.strip(), sep = '\n')
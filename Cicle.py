listok = []
list = []
for i in range (97,123):
    b = chr(i)
    listok.append(b)
for i in range(26):
    b = (i+1) * listok[i]
    list.append(b)
print(list)

letter = 'а'
n = input()+" запретил букву "
s = n
parus = []
for i in range (len(n)):
    if n[i] not in parus:
        if n[i] != ' ':
            parus.append(n[i])
            parus.sort()
for j in range (len(parus)):
    s = s.replace('  ',' ')
    print(s.lstrip(),parus[j])
    s = s.replace(parus[j],'')
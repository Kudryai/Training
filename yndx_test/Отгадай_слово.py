s, q = [c for c in input()],[c for c in input()] #Необходимо дополнительно покрыть тестами
lst = []
a = 0
b = 0
bol = 1
while b != len(q):
    cnt = s.count(q[b])
    if cnt >= 2:
        bol = cnt
    if s[a] == q[b]:
        if a == b:
            lst += ['correct']
            s[a] = '*'
            b += 1
            a = 0
    if b == len(s):
        break
    if s[a] == q[b] and b != len(s):
        if a != b and s[a] != q[a]:
            lst += ['present']
            s[a] = '*'
            b += 1
            a = 0
    if cnt == 0 or a == len(s):
        if s[a] != '*' and s[a] != q[a]:
            b += 1
            lst += ['absent']
            s[a] = '*'
            a = 0
    a += 1
    if a == len(q):
        lst += ['absent']
        s[a] = '*'
        a = 0
        b += 1
        if b == len(q):
            break

print(*lst, sep = '\n')
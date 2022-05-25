n = input().split()
l = []
l.extend(n)
b = []
for num in l:
    b.append(int(num))
mn = min(b)
mx = max(b)
p1mn = b.index(mn)
p1mx = b.index(mx)
b.insert(p1mn, mx)
b.pop(p1mn+1)
b.insert(p1mx, mn)
b.pop(p1mx+1)
print(*b)
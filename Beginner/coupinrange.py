n = input()
b = n.find('h')+1
c = n.rfind('h')
d = n[b:c]
cout = d[::-1]
g = n[:b] + cout + n[c:]
print(g)
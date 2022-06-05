b = int(input())
cont = int((b+1)/2)
for i in range(b):
        for j in range (i+1):
            print('*', end ="")
        print()
        if i == cont-1:
            break
for k in range(cont-1):
        for l in range (k,i):
            print('*', end ="")
        print()
print(k,b)
            
        
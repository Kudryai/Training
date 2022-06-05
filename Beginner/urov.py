n = int(input())
cont = 0
for k in range (1,n+1):
    for i in range (1,k):
        print (i, end ="")
    for j in range (k,0,-1):
        print(j, end ="")
    print()
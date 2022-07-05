nm = input().split()

def print_mx(n,m):
    cont = 1
    for i in range(1,n+1):
        for j in range(cont,m+cont):
            print(j,end = " ")
        print()
        cont += m

print_mx(int(nm[0]),int(nm[-1]))
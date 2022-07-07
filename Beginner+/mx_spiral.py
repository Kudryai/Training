nm = input().split()
mx_rep = []

q = 0
z = 1
m = 1

def matrix(n,m):
    strt = 1
    for i in range(1,n+1):
        list1 = []
        for j in range(strt,m+strt):
            list1.append(j)
        mx_rep.append(list1)
    if n == 1: 
        return print_mx(mx_rep)
    return edit_mx(mx_rep,z,q,strt)

        
def edit_mx(list,z,q,m): #Печать матрицы
    for i in range(q,int(nm[0])-q):
        for j in range(q,int(nm[-1])-q):
            if i == q and j >= q:
                list[i][j] = m
                m += 1
                if m == int(nm[0])*int(nm[-1])+1:
                    return print_mx(list)
            if i > q and j == int(nm[-1]) - z:
                list[i][j] = m
                m += 1
          
    return edit_mx2(list,int(nm[0]),int(nm[-1]),m,z,q)


def edit_mx2(list,n,m,start,z,q):
    for i in range(n-z,q,-1):
        for j in range(m-(2+q),-1+q,-1):
            if i == n-z:
                list[i][j] = start
                start += 1
                if start == n*m+1:
                    return print_mx(list)
            if n - z > i > q and j == q:
                list[i][j] = start
                start += 1
                if start == n*m+1:
                    return print_mx(list)
    z += 1
    q += 1
    if start == n*m+1:
        return print_mx(list)
    return edit_mx(list,z,q,start)
def print_mx(list): #Печать матрицы
    for i in range(int(nm[0])):
        for j in range(int(nm[-1])):
            print(str(list[i][j]).ljust(3),end = " ")
        print()

matrix(int(nm[0]),int(nm[-1]))
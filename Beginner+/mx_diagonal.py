nm = input().split()
mx_rep = []


def matrix(n,m):
    strt = 1
    for i in range(1,n+1):
        list1 = []
        for j in range(strt,m+strt):
            list1.append(j)
        mx_rep.append(list1)
        strt = int(list1[-1])+1
    return edit_mx(mx_rep)

        
def edit_mx(list): #Печать матрицы
    l = 0
    m = 1
    for _ in range(int(nm[0])+int(nm[-1])-1):
        for i in range(int(nm[0])):
            for j in range(int(nm[-1])):
                if i + j == l:
                  list[i][j] = m
                  m += 1
        l += 1
          
    return print_mx(mx_rep)


def print_mx(list): #Печать матрицы
    for i in range(int(nm[0])):
        for j in range(int(nm[-1])):
            print(str(list[i][j]).ljust(3),end = " ")
        print()

matrix(int(nm[0]),int(nm[-1]))
nm = input().split()
mx_rep = []


def matrix(n,m):
    for i in range(1,n+1):
        list1 = [i]
        for j in range(m-1):
            list1.append(int(list1[j])+n)
        mx_rep.append(list1)
    return print_mx(mx_rep)

def print_mx(list): #Печать матрицы
    for i in range(int(nm[0])):
        for j in range(int(nm[-1])):
            print(str(list[i][j]).ljust(3),end = " ")
        print()


matrix(int(nm[0]),int(nm[-1]))



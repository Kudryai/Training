nm = input().split()
mx_rep = []


def matrix(n,m):
    for i in range(1,n+1):
        list1 = []
        for j in range(1,m+1):
            list1.append(j)
        mx_rep.append(list1)
        return edit_mx(mx_rep,n,m)


def edit_mx(list,n,m):
    edit_mx_lst = list[0].copy()
    list_glv = list.copy()
    for i in range(n-1):
        sy = edit_mx_lst.pop(0)
        edit_mx_lst.insert(m,sy)
        list_glv.append(edit_mx_lst.copy())
    return print_mx(list_glv)

        
def print_mx(list): #Печать матрицы
    for i in range(int(nm[0])):
        for j in range(int(nm[-1])):
            print(str(list[i][j]).ljust(3),end = " ")
        print()


matrix(int(nm[0]),int(nm[-1]))



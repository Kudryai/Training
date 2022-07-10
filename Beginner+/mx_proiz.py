
mx_A = []
mx_B = []
mx_C = []

def matrix(key):
    if key == 1:
        nm = input().split()
        n,m = int(nm[0]),int(nm[-1])
        for _ in range(n):
            list1 = input().split()
            mx_A.append(list1)
        input()
        return matrix(2)
    if key == 2:
        nm = input().split()
        n1,m1 = int(nm[0]),int(nm[-1])
        for _ in range(n1):
            list2 = input().split()
            mx_B.append(list2.copy())
        list2.clear()
        for i in range(m1):
            rev = []
            for j in range(n1):
                rev.append(mx_B[j][i])
            list2.append(rev)
    return edit_mx(mx_A,list2,m1,n1,0)

        
def edit_mx(list1,list2,row,column,key): #Произведение матрицы
    a = key
    for i in range(row):
        b = 0
        sum_list = []
        for j in range(column):
            sum2 = int(list1[a][b]) * int(list2[i][j])
            b += 1
            sum_list.append(sum2)
        mx_C.append(sum_list.copy())
    a += 1
    if a == row:
        list_glav = []
        sum_list.clear()
        z = 0
        for i in range(row):
            sum_list = []
            for j in range(z,row+z):
                g = sum(mx_C[j])
                sum_list.append(g)
            z += row
            list_glav.append(sum_list.copy())
        return print_mx(list_glav,row,column)
    else:
        return edit_mx(list1,list2,row,column,a)


def print_mx(list,n,m): #Печать матрицы
    for i in range(n):
        for j in range(n):
            print(str(list[i][j]).ljust(6),end = "")
        print()

matrix(1)
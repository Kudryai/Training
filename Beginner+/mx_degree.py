n = int(input())
mx_A = []
mx_B = []
mx_C = []


def matrix(n,m,key,list,itr,de):
    degr = de
    mx_B = list
    if key != 1:
        for _ in range(n):
            list1 = input().split()
            mx_A.append(list1)
            mx_B = mx_A.copy()
        itr = int(input())
    list2 = []
    for i in range(n):
        rev = []
        for j in range(n):
            rev.append(mx_B[j][i])
        list2.append(rev)
    return edit_mx(mx_A,list2,n,0,itr,degr)

        
def edit_mx(list1,list2,rc,key,itr,degr): #Произведение матрицы
    a = key
    for i in range(rc):
        b = 0
        sum_list = []
        for j in range(rc):
            sum2 = int(list1[a][b]) * int(list2[i][j])
            b += 1
            sum_list.append(sum2)
        mx_C.append(sum_list.copy())
    a += 1
    if a == rc:
        list_glav = []
        sum_list.clear()
        z = 0
        for i in range(rc):
            sum_list = []
            for j in range(z,rc+z):
                g = sum(mx_C[j])
                sum_list.append(g)
            z += rc
            list_glav.append(sum_list.copy())
        degr += 1
        return print_mx(list_glav,rc,rc,degr,itr)
    else:
        return edit_mx(list1,list2,rc,a,itr,degr)


def print_mx(list,n,m,de,itr):
    if de != int(itr) - 1: #Печать матрицы
        mx_C.clear()
        return matrix(n,n,1,list,itr,de)
    for i in range(n):
        for j in range(n):
            print(str(list[i][j]).ljust(10),end = "")
        print()

matrix(n,n,0,[],0,0)
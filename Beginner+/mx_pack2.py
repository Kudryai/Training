n = int(input())
mx_rep = []


def matrix(n):
    for i in range(n):
        list1 = []
        for j in range(n):
            if j == i or i < j and j < n-i-1:
                list1.append('1')
            elif j == n-i-1 or i > j and j > n-i-1:
                list1.append('1')
            else:
                list1.append('0')
        mx_rep.append(list1)
    return print_mx(mx_rep)

def print_mx(list): #Печать матрицы
    for i in range(n):
        for j in range(n):
            print(str(list[i][j]).ljust(3),end = " ")
        print()


matrix(n)



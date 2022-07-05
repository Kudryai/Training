nm = input().split()

def mx_list(n,m): # Сборк списка
    multi = []
    glav = []
    count = 0
    for i in range(n):
        for j in range(m):
            if j%2 == 0 and count%2 == 0:
                multi.append('.')
            else:
                multi.append('*')
            
        if count%2 == 0:
            glav.append(multi)
        else:
            glav.append(multi[::-1])
        count += 1
    return glav

    # for j in range(1,m+1):
    #     if j%2 == 0:
    #         multi.append('*')
    #     else:
    #         multi.append('.')
    # for i in range(n):
    #     if count%2 == 0:
    #         glav.append(multi)
    #     else:
    #         glav.append(multi[::-1])
    #     count += 1
    # return glav

list_mx = mx_list(int(nm[0]),int(nm[-1]))

def print_mx(list):
    for i in range(int(nm[0])):
        for j in range(int(nm[-1])):
            print(list_mx[i][j],end = " ")
        print()

print_mx(list_mx)

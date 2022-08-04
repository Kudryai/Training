with open(input()) as file:
    data = list(map(str.strip,file.read().split()))
    res = []
    great = []
    z = 0
    for i in range(len(data)):
        if data[i] == 'def' or data[i] == '#':
            ded = [data[i],i]
            res.append(ded)
    for num in res:
        if num[0] == 'def':
            z -= 1
        if num[0] == '#':
            z += 1
        if z == 2 or z == -1:
            z = 0
            great.append(data[num[1]+1])
if len(great)>1:
    for du in great:
        func_name = ''
        for z in du:
            if z != '(':
                func_name += z
            else:
                print(func_name)
                break
else:
    print('Best Programming Team')




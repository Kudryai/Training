txt = input().split()
list_list = [[],]
list_wor = []

def chunk(text):
    if len(list_wor) <= 1:
        for i in range(len(text)):
            list_wor.append([text[i]])
            list_list.append([text[i]])
        if len(text) == 1:
            return print(list_list)
        else:
            return chunk(list_wor)
    elif len(list_wor[0]) <= 1:
        list_pass = []
        for i in range(len(text)-1):
            if len(text)-1 != i:
                list_pass.append(*text[i])
                list_pass.append(*text[i+1])
                lis = list_pass.copy()
                list_list.append(lis)
                list_wor.append(list_pass)
                list_pass = []              
        del list_wor[0:len(txt)]
        return chunk2(txt)

def chunk2(text):
    if len(txt) != len(list_wor[-1]):
        for i in range(len(list_wor)):
            if len(list_wor)-1 != i:
                list_wor[i].append(txt[len(list_wor[i])+i])
                lis = list_wor[i].copy()
                list_list.append(lis)
            else:
                del list_wor[-1]
        return chunk2(list_list)
    else:
        return print(list_list)


chunk(txt)
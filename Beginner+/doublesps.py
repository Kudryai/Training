txt = input().split(' ')

def spisokdouble(text):
    listres1 = []
    listdoub = []
    for i in range(len(text)):  # w w w o p r
        if i+1 != len(text):
            if text[i+1] == text[i]:
                listdoub.append(text[i])

            else:
                listdoub.append(text[i])
                listres1.append(listdoub)
                listdoub = []
                if listres1[-1][-1] != text[i]:
                    listres1.append([text[i]])
        else:
            if len(listdoub) > 0:
                listdoub.append(text[i])
                listres1.append(listdoub)
            elif len(listdoub) == 0:
                listres1.append([text[i]])

    return print(listres1)

spisokdouble(txt)
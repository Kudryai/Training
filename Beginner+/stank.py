txt = input().split()
n = int(input())
list1 = []

def chunk(text,n):
    list2 = []
    if len(text) >= n:
        for i in range(n):
            list2.append(text[i])
        del text[0:i+1]
        list1.append(list2)
        if len(text) != 0:
            return chunk(text,n)
        else:
            return print(list1)
    else:
        list1.append(text)
        return print(list1)

chunk(txt,n)
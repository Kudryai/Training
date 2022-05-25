def merge(list1,list2):
    alllist = list1 + list2
    alllist.sort()
    return alllist

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1,numbers2))
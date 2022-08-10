def index_of_nearest(numbers,number):
    lister = []
    if len(numbers) == 0:
        return -1
    for i in range(len(numbers)):
        test1 = number - i
        test2 = number + i
        for j in range(len(numbers)):
            if len(lister) == 2:
                break
            if test1 == numbers[j]:
                lister.append(numbers[j])
            if test2 == numbers[j]:
                lister.append(numbers[j])
    if len(lister) == 1:
        return numbers.index(lister[0])
    else:
        a = number - lister[0]
        b = number - lister[1]
        if a <= b:
            return numbers.index(lister[0])
        else:
            return numbers.index(lister[1])

            
print(index_of_nearest([1, 14, 100, 65, 6], 5))
print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
print(index_of_nearest([1, 1, 1, 1, 1], 1))
print(index_of_nearest([10, 99, 0, -12, 16], -9))
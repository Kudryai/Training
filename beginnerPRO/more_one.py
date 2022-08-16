# Дана последовательность неотрицательных целых чисел. Напишите программу, 
# которая выводит те числа, которые встречаются в данной последовательности более одного раза.

main_numbers = [i for i in input().split()]
result = set(filter(lambda x: x if main_numbers.count(x) > 1 else False, main_numbers))
print(*sorted(result))
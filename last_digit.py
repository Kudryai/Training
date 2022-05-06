num=int(input())
last_digit = num%10 #Последняя цифра
first_digit = num//10 #Первая цифра
if last_digit == first_digit:
    print("YES")
else:
    print('No')
    
n = input()
total1 = 0
total2 = 0
for c in n:
    if c == "*":
        total1 +=1
    if c == "+":
        total2 +=1
print('Символ + встречается', total2,'раз')
print('Символ * встречается', total1,'раз')
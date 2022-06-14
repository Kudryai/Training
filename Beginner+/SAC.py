num = input() 
for i in range(len(num)-3,0,-3): # Standart American Convention
    num = num[:i] + ',' + num[i:]
print(num)
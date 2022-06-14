def get_next_prime(num):
    for i in range(num,num+10):
        if is_prime(i):
            if i > num:
                return i
    
def is_prime(num):
    delit = 0
    for i in range(1,num+1):
        if num%i == 0:
            delit += 1
    if delit == 2:
        return True
    else:
        return False
        
# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
# объявление функции
def is_valid_password(password):
    a = 0
    b = 0
    c = 0
    if is_palindrome(psw[0]) == True:
        a += 1
    if is_prime(int(psw[1])) == True:
        b += 1
    if is_even(int(psw[2])) == True:
        c += 1
    if a >= 1 and b >= 1 and c >= 1 and len(password) < 4:
        return True
    else:
        return False
def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
def is_palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False
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
psw = input().split(':')

# вызываем функцию
print(is_valid_password(psw))
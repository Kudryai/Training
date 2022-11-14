import random

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_lenght = min_length
        self.max_length = max_length
    
    def __call__(self, *args, **kwds) -> str:
        num_rand = random.randint(self.min_lenght, self.max_length)
        string = ''
        for _ in range(num_rand):
            string += random.choice(self.psw_chars)
        return string
        

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for i in range(3)]
print(lst_pass)
# объявление функции
def draw_triangle():
    for i in range(9):
        print(' '* (9 -1 -i) + '*' * (1 + i * 2))

# основная программа
draw_triangle()  # вызов функции
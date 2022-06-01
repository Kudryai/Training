from random import *
print('Приветствую тебя, я MagicBall и я готов дать ответ на любой твой вопрос.')
name = input('Назови своё имя:')
print(f'Привет {name}!')
game = 1
answers = ['Беспорно','Предрешено','Никаких сомнений','Определённо да', 
'Можешь быть уверен в этом','Мне кажется - да','Вероятнее всего',
'Хорошие перспективы','Знаки говорят - да','Да','Пока неясно,попробуй снова',
'Спроси позже','Лучше не рассказывать','Сейчас нельзя предсказать',
'Сконцентрируйся и спроси опять','Даже не думай','Мой ответ - нет',
'По моим данным - нет','Перспективы не очень хорошие','Весьма сомнительно']

def conti(y_n):
    if y_n == 'y':
        return main_brain(name,answers,0)
    if y_n == 'n':
        print('Пока,пока!')
        global game
        game = 0
    else:
        return main_brain(name,answers,99)


def main_brain(name,answerlist,err):
    while game == 1:
        if game == 1 and err != 99:
            answer = input(f'Какой твой вопрос {name}? ->')
            print(choice(answerlist))
            y_n = input(f'Есть еще вопросы {name}? (Y или N):').lower()
            return conti(y_n)
        if err == 99:
            y_n = input(f'{name} неправильно ввел данные!(Y - продолжить  или N - закончить):').lower()
            return conti(y_n)
    
main_brain(name,answers,0)

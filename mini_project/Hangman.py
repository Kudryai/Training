from random import *
word_list = ['БАНАН','АРБУЗ','ЛАДОГА','ШАШЛЫК','ЛЕТО']

def get_word():
    return play(choice(word_list))

def display_hangman(tries):
    stages = ['''
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     / \\
                 - ЭТО КОНЕЦ!
              ''',
              '''
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     / 
                 -
              ''',
              '''
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |      
                 -
              ''',
              '''
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      
                 |      
                 -
              ''',
              '''
                 --------
                 |      |
                 |      O
                 |      |/
                 |      
                 |      
                 -
              ''',
              '''
                 --------
                 |      |
                 |      O
                 |      |
                 |      
                 |      
                 -
              ''',
              '''
                 --------
                 |      |
                 |      O
                 |     
                 |      
                 |      
                 -
              ''',
              '''
                 --------
                 |      |
                 |      
                 |     
                 |      
                 |      
                 -
              ''']
    return stages[tries]


def check(buk):
   if buk.isalpha() == True:
      return True
   if buk.isalpha() == False:
      return False


def play(word):
   word_completion = '_' * len(word)
   guessed = False
   guessed_letters = []
   guessed_words = []
   tries = 7
   print('Угадай слово или будешь висеть!')
   while True:
      if tries != 0:
         print(display_hangman(tries))
         print(f'''
               {word_completion}
             ^^Слово^^
          ''')
         slovo = input('Введите букву или слово:').upper()
      if check(slovo) == True:
         if len(slovo) == len(word):
            if slovo in guessed_words:
               print('Такое слово уже было, попробуйте снова')
            else:
               guessed_words += slovo
               if slovo == word:
                  print('Поздравляем вы угадали!')
                  break
               if slovo != word:
                  print('Неправильное слово, попробуйте снова')
                  tries -= 1
                  continue
         if len(slovo) == 1:
            if slovo in guessed_letters:
               print('Данная буква уже была')
            else:
               guessed_letters += slovo
               if slovo in word:
                  print('Вы угадали')
                  for i in range(len(word)):
                     if word[i] == slovo:
                        word_completion = word_completion[:i] + slovo + word_completion[(i+1):]
                        if word_completion == word:
                           print()
                           print(display_hangman(tries))
                           print(f'''
               {word_completion}
             ^^Слово^^
          ''')
                           print("++++++++++++++++++++++++++++++")
                           print(f'Вы победили!Загаданное слово {word}')
                           print("++++++++++++++++++++++++++++++")
                           while True:
                              cont = input('Еще разок? y/n').upper()
                              if cont == 'Y':
                                 return get_word()
                              if cont == 'N':
                                 return False
                              else:
                                 print('Ввел чушь какую то. Пока')
                                 return False
               else:
                  print('Такой буквы нет, выберите другую')
                  tries -= 1
                  continue
      if tries == 0:
         print()
         print(display_hangman(tries))
         print('     ~~~~~~Тебя повесили~~~~   ')
         print(f'~ Загаданное слово  {word} ~')
         while True:
            cont = input('Еще разок? y/n').upper()
            if cont == 'Y':
               return get_word()
            if cont == 'N':
               return False
            else:
               print('Ввел чушь какую то. Пока')
               return False
      if check(slovo) == False:
         print('~Только буквы или слово~')
         continue
get_word()
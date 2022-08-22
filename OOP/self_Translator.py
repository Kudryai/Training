class Translator: # Переводчик слов.
    word = {}
    def add(self, eng, rus):
        if self.word.get(eng, False):
            if rus not in self.word[eng]:
               self.word[eng] = self.word.get(eng, []) + [rus] 
        else:
            self.word[eng] = self.word.get(eng, []) + [rus]

    def remove(self, eng):
        del self.word[eng]


    def translate(self, eng):
        return self.word[eng]

tr = Translator()
tr.add('tree','дерево')
tr.add('car','машина')
tr.add('car','автомобиль')
tr.add('leaf','лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go','ходить')
tr.add('milk', 'молоко')
tr.remove('car')
print(*tr.translate('go'))

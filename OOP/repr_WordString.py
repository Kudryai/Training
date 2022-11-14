class WordString:
    list_str = []


    def __init__(self, strings='') -> None:
        self.strings = strings
        self.list_str = strings.split()

    def __len__(self):
        return len(self.list_str)

    def __call__(self, indx) -> str:
        return self.list_str[indx]

    @property
    def string(self):
        return self.strings

    @string.setter
    def string(self, txt):
        self.strings = txt
        self.list_str = txt.split()

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
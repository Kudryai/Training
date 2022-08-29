import sys

class StreamData:
  def create(self, fields, lst_values):
    if len(fields) == len(lst_values):
        for i in range(len(fields)):
            setattr(self,fields[i], lst_values[i])
        return True
    return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return print(sd.__dict__, res)


sr = StreamReader()
data, result = sr.readlines()
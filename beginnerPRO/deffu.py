def same_parity(data): 
  # # Функция должна возвращать новый список, 
  # элементами которого являются числа из списка numbers, 
  # имеющие ту же четность, что и первый элемент этого списка.
   if len(data) == 0:
     return data
   if int(data[0])%2 == 0:
       resche = list(filter(lambda x: str(x) if x%2 == 0 or x == 0 else False,data))
       return resche
   else:
       resnig = list(filter(lambda x: x if x == 0 or x%2 != 0 else False,data))
       return resnig
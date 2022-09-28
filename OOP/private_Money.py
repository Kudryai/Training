class Money:

  def __init__(self, money=0):
    self.__money = money

  def set_money(self,money):
    if self.__check_money(money):
      self.__money = money

  def get_money(self):
    return self.__money

  def add_money(self,mn):
    self.__money += mn.__money
  
  @classmethod
  def __check_money(self,money):
    if type(money) == int:
      if money >= 0:
        return True
    return False

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(-1)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120
class  Clock:
    
    def __init__(self,time):
        self.__time = 0
        if self.__check_time(time):
            self.__time = time
    
    def set_time(self,tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls,tm):
        if type(tm) == int:
            if 0 <= tm <= 100000:
                return True
        return False


clock = Clock(4530)
clock.set_time = 300
print(clock.get_time)
class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self,obj):
        self.__prev = obj


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if self.tail:
            self.tail.next = obj
        obj.prev = self.tail
        self.tail = obj
        if not self.top:
            self.top = obj

    def pop(self):
        pop = self.tail
        if self.tail is None:
            return
        prev = self.tail.prev
        if prev:
            prev.next = None
        self.tail = prev
        if self.tail is None:
            self.top = None
        return pop
    def get_data(self):
        s = []
        h = self.top
        while h:
            s.append(h.data)
            h = h.next
        return s


s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()
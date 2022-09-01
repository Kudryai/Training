class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj

lst_in = ['1.7 Методы класса (classmethod) и статические методы (staticmethod)', '1.4 Методы классов. Параметр self']

head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj)
    onj = obj_new

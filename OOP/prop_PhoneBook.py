class PhoneBook:
    number_list = []

    def add_phone(self, phone):
        self.number_list.append(phone)

    def remove_phone(self, indx):
        del self.number_list[indx]

    def get_phone_list(self):
        return self.number_list


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones[1].fio)

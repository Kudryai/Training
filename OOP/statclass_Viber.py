class Viber:
    message = {}
    cnt = 0

    @classmethod
    def add_message(cls,msg):
        cls.message[cls.cnt] = cls.message.get(cls.cnt, msg)
        cls.cnt += 1

    @classmethod
    def remove_message(cls,msg):
        for i in range(len(cls.message)):
            if cls.message[i].text == msg.text:
                del cls.message[i]

    def set_like(msg):
        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @classmethod
    def show_last_message(cls,число):
        return cls.message[число].text

    @classmethod
    def total_messages(cls):
        return len(cls.message)

class Message:

    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like




msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
print(Viber.total_messages())
Viber.set_like(msg)
Viber.remove_message(msg)
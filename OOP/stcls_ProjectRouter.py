from random import randint

class Server:

    def __init__(self):
        self.ip = randint(0,100)
        self.buffer = []
    def send_data(self,data):
        router.buffer.append(data)

    def get_data(self):
        a = self.buffer
        self.buffer = []
        return a


    def get_ip(self):
        return self.ip

    def __del__(self):
        self.buffer = []

class Router:

    def __init__(self):
        self.buffer = []
        self.servers = []

    def link(self,server):
        self.servers.append(server)


    def unlink(self,server):
        for k in range(len(self.servers)):
            if self.servers[k].ip == server.ip:
                del self.servers[k]

    def send_data(self):
        for i in range(len(self.servers)):
            for j in range(len(self.buffer)):
                if self.servers[i].ip == self.buffer[j].ip:
                    self.servers[i].buffer.append(self.buffer[j])
        self.buffer = []
        self.servers = []
class Data:
    def __init__(self,str,ip):
        self.data = str
        self.ip = ip




router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_from[0].data, msg_lst_to[0].data)
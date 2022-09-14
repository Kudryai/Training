class AppStore:
    stores_len = {}

    def add_application(self, app):
        self.stores_len[app.name] = self.stores_len.get(app.name, app.blocked)

    def remove_application(self, app):
        del self.stores_len[app.name]

    def block_application(self, app):
        self.stores_len[app.name] = True
        app.blocked = True

    def total_apps(self):
        return len(self.stores_len)

class Application:

    def __init__(self, name,blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
app_youtube2 = Application("Youtube2")
store.add_application(app_youtube)
store.block_application(app_youtube)
store.add_application(app_youtube2)
store.block_application(app_youtube2)
store.remove_application(app_youtube)
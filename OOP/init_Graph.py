class Graph:
    def __init__(self, data, is_show = True):
        self.data = data.copy()
        self.is_show = is_show

    def set_data(self, data):
        self.data = data
    def show_table(self):
        if self.is_show == False:
            return print("Отображение данных закрыто")
        a = [str(i) for i in self.data]
        print(' '.join(a))
    def show_graph(self):
        if self.is_show == False:
            return print("Отображение данных закрыто")
        a = [str(i) for i in self.data]
        print(f"Графическое отображение данных: {' '.join(a)}")
    def show_bar(self):
        if self.is_show == False:
            return print("Отображение данных закрыто")
        a = [str(i) for i in self.data]
        print(f"Столбчатая диаграмма: {' '.join(a)}")
    def set_show(self, fl_show):
        self.is_show = fl_show

data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show = False)
gr.show_table()
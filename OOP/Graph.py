class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        return print(
            *list(
                filter(
                    lambda x: str(x)
                    if int(self.LIMIT_Y[0]) <= x <= int(self.LIMIT_Y[1])
                    else False,
                    self.data,
                )
            )
        )


graph1 = Graph()
graph1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph1.draw()

class PolyLine:
    def __init__(self, *args):
        self.coords = []
        for coord in args:
            self.coords.append(coord)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        del self.coords[indx]

    def get_coords(self):
        return self.coords

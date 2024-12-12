class AoCY2024D06:

    def __init__(self):
        self.mapa = self.get_map()
        self.x, self.y = self.get_start()

    def get_map(self):
        with open('inputs/06.txt') as file:
            return tuple(tuple(line.strip()) for line in file)

    def get_start(self):
        for y, row in enumerate(self.mapa):
            for x, val in enumerate(row):
                if '^' == val:
                    return x, y
        return 0, 0

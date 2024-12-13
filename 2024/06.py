class AoCY2024D06:

    def __init__(self):
        self.mapa = self.get_map()
        self.limit_y = len(self.mapa)
        self.limit_x = len(self.mapa[0])
        self.steps = {
            'N': (0, -1, 'E'),
            'E': (1, 0, 'S'),
            'S': (0, 1, 'W'),
            'W': (-1, 0, 'N'),
        }

    def get_map(self):
        with open('inputs/06.txt') as file:
            return tuple(tuple(line.strip()) for line in file)

    def get_start(self):
        for y, row in enumerate(self.mapa):
            for x, val in enumerate(row):
                if '^' == val:
                    return x, y
        return 0, 0

    def get_next_pos(self, pos_x, pos_y, direction):
        x = pos_x
        y = pos_y
        step_x, step_y, new_dir = self.steps[direction]
        x += step_x
        y += step_y
        if x < 0 or y < 0 or x >= self.limit_x or y >= self.limit_y:
            return False
        if '#' == self.mapa[y][x]:
            return self.get_next_pos(pos_x, pos_y, new_dir)
        return x, y, direction

    def get_part1(self):
        direction = 'N'
        x, y = self.get_start()
        visited = {f"{x},{y}"}
        while True:
            val = self.get_next_pos(x, y, direction)
            if val is False:
                break
            x = val[0]
            y = val[1]
            direction = val[2]
            visited.add(f"{x},{y}")
        return len(visited)


aoc = AoCY2024D06()
print('Answer 1:', aoc.get_part1())

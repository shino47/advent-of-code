class AoCY2024D06:

    def __init__(self):
        self.mapa = self.get_map()
        self.limit_y = len(self.mapa)
        self.limit_x = len(self.mapa[0])
        self.block_char = '#'
        self.free_char = '.'
        self.start_char = '^'
        self.start_dir = 'N'
        self.start_x, self.start_y = self.get_start()
        self.steps = {
            'N': (0, -1, 'E'),
            'E': (1, 0, 'S'),
            'S': (0, 1, 'W'),
            'W': (-1, 0, 'N'),
        }

    def get_map(self):
        with open('inputs/06.txt') as file:
            return [list(line.strip()) for line in file]

    def get_start(self):
        for y, row in enumerate(self.mapa):
            for x, val in enumerate(row):
                if self.start_char == val:
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
        if self.mapa[y][x] == self.block_char:
            return self.get_next_pos(pos_x, pos_y, new_dir)
        return x, y, direction

    def get_part1(self):
        direction = self.start_dir
        x = self.start_x
        y = self.start_y
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

    def test_path(self):
        direction = self.start_dir
        x = self.start_x
        y = self.start_y
        corners = ''
        lasts = []
        while True:
            val = self.get_next_pos(x, y, direction)
            if val is False:
                break
            x = val[0]
            y = val[1]
            pos = f"{x},{y}"
            if direction != val[2]:
                lasts.append(pos)
                corners += f"|{pos}"
                if len(lasts) >= 2:
                    if corners.count('|'.join(lasts)) >= 2:
                        return True
                    lasts.pop(0)
            direction = val[2]
        return False

    def get_part2(self):
        paths = 0
        for y, row in enumerate(self.mapa):
            for x, char in enumerate(row):
                if char != self.free_char:
                    continue
                self.mapa[y][x] = self.block_char
                if self.test_path():
                    paths += 1
                self.mapa[y][x] = self.free_char
        return paths


aoc = AoCY2024D06()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

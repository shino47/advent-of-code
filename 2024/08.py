import re


class AoCY2024D08:

    def __init__(self):
        self.input = self.get_input()
        self.limit_y = len(self.input)
        self.limit_x = len(self.input[0])
        self.antennas = []
        self.antinodes = set()

    def get_input(self):
        with open('inputs/08.txt') as file:
            return tuple(tuple(line.strip()) for line in file)

    def set_antinode(self, x, y, dist_x, dist_y, up=False, extended=False):
        an_x = (x - dist_x) if up else (x + dist_x)
        an_y = (y - dist_y) if up else (y + dist_y)
        if an_x >= 0 and an_x < self.limit_x and an_y >= 0 and an_y < self.limit_y:
            self.antinodes.add(f'{an_x},{an_y}')
            if extended:
                self.set_antinode(an_x, an_y, dist_x, dist_y, extended)

    def find_pairs(self, char, x1, y1, extended=False):
        for y2 in range(y1, self.limit_y):
            for x2 in range((x1 + 1) if y1 == y2 else 0, self.limit_x):
                if self.input[y2][x2] == char:
                    dist_x = x2 - x1
                    dist_y = y2 - y1
                    self.set_antinode(x1, y1, dist_x, dist_y, True, extended)
                    self.set_antinode(x2, y2, dist_x, dist_y, False, extended)

    def scan_map(self, extended):
        self.antennas = []
        self.antinodes = set()
        for y, row in enumerate(self.input):
            for x, char in enumerate(row):
                if re.match(r'[0-9a-zA-Z]', char):
                    self.antennas.append(char)
                    self.find_pairs(char, x, y, extended)

    def get_part1(self):
        self.scan_map(False)
        return len(self.antinodes)

    def get_part2(self):
        self.scan_map(True)
        return len(self.antinodes) + len(self.antennas)


aoc = AoCY2024D08()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

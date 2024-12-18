import re


class AoCY2024D08:

    def __init__(self):
        self.input = self.get_input()
        self.limit_y = len(self.input)
        self.limit_x = len(self.input[0])
        self.antinodes = set()

    def get_input(self):
        with open('inputs/08.txt') as file:
            return tuple(tuple(line.strip()) for line in file)

    def set_antinodes(self, x1, y1, x2, y2):
        dist_x = x2 - x1
        dist_y = y2 - y1
        an1_x = x1 - dist_x
        an1_y = y1 - dist_y
        an2_x = x2 + dist_x
        an2_y = y2 + dist_y
        if an1_x >= 0 and an1_x < self.limit_x and an1_y >= 0 and an1_y < self.limit_y:
            self.antinodes.add(f'{an1_x},{an1_y}')
        if an2_x >= 0 and an2_x < self.limit_x and an2_y >= 0 and an2_y < self.limit_y:
            self.antinodes.add(f'{an2_x},{an2_y}')

    def find_pairs(self, char, x1, y1):
        for y2 in range(y1, self.limit_y):
            for x2 in range((x1 + 1) if y1 == y2 else 0, self.limit_x):
                if self.input[y2][x2] == char:
                    self.set_antinodes(x1, y1, x2, y2)

    def get_part1(self):
        for y, row in enumerate(self.input):
            for x, char in enumerate(row):
                if re.match(r'[0-9a-zA-Z]', char):
                    self.find_pairs(char, x, y)
        return len(self.antinodes)

    def get_part2(self):
        pass


aoc = AoCY2024D08()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

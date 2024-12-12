class AoCY2024D04:

    def __init__(self):
        self.key = ('X', 'M', 'A', 'S')
        self.key_len = len(self.key)
        self.middle = 'A'
        self.start = 'M'
        self.end = 'S'
        self.input = self.get_input()
        self.limit_y = len(self.input)
        self.limit_x = self.limit_y

    def get_input(self):
        with open('inputs/04.txt') as file:
            return tuple(tuple(line.strip()) for line in file)

    def has_east(self, x, y):
        if (self.key_len + x) > self.limit_x:
            return False
        for n, letter in enumerate(self.key):
            if self.input[y][x + n] != letter:
                return False
        return True

    def has_south(self, x, y):
        if (self.key_len + y) > self.limit_y:
            return False
        for n, letter in enumerate(self.key):
            if self.input[y + n][x] != letter:
                return False
        return True

    def has_west(self, x, y):
        if (x - self.key_len + 1) < 0:
            return False
        for n, letter in enumerate(self.key):
            if self.input[y][x - n] != letter:
                return False
        return True

    def has_north(self, x, y):
        if (y - self.key_len + 1) < 0:
            return False
        for n, letter in enumerate(self.key):
            if self.input[y - n][x] != letter:
                return False
        return True

    def has_south_east(self, x, y):
        if (self.key_len + x) > self.limit_x or (self.key_len + y) > self.limit_y:
            return False
        for n, letter in enumerate(self.key):
            if self.input[y + n][x + n] != letter:
                return False
        return True

    def has_south_west(self, x, y):
        if (x - self.key_len + 1) < 0 or (self.key_len + y) > self.limit_y:
            return False
        for n, letter in enumerate(self.key):
            if self.input[y + n][x - n] != letter:
                return False
        return True

    def has_north_east(self, x, y):
        if (self.key_len + x) > self.limit_x or (y - self.key_len + 1) < 0:
            return False
        for n, letter in enumerate(self.key):
            if self.input[y - n][x + n] != letter:
                return False
        return True

    def has_north_west(self, x, y):
        if (x - self.key_len + 1) < 0 or (y - self.key_len + 1) < 0:
            return False
        for n, letter in enumerate(self.key):
            if self.input[y - n][x - n] != letter:
                return False
        return True

    def get_dirs_qty(self, x, y):
        values = [
            self.has_east(x, y),
            self.has_south(x, y),
            self.has_west(x, y),
            self.has_north(x, y),
            self.has_south_east(x, y),
            self.has_south_west(x, y),
            self.has_north_east(x, y),
            self.has_north_west(x, y),
        ]
        return len([valid for valid in values if valid])

    def get_part1(self):
        count = 0
        for y, row in enumerate(self.input):
            self.limit_x = len(row)
            for x, letter in enumerate(row):
                if self.key[0] == letter:
                    count += self.get_dirs_qty(x, y)
        return count

    def has_q1_to_q3(self, x, y):
        return self.start == self.input[y - 1][x + 1] and self.end == self.input[y + 1][x - 1]

    def has_q3_to_q1(self, x, y):
        return self.start == self.input[y + 1][x - 1] and self.end == self.input[y - 1][x + 1]

    def has_q2_to_q4(self, x, y):
        return self.start == self.input[y - 1][x - 1] and self.end == self.input[y + 1][x + 1]

    def has_q4_to_q2(self, x, y):
        return self.start == self.input[y + 1][x + 1] and self.end == self.input[y - 1][x - 1]

    def is_valid_cross(self, x, y):
        if (x - 1) < 0 or (y - 1) < 0 or (x + 1) >= self.limit_x or (y + 1) >= self.limit_y:
            return False
        return (self.has_q1_to_q3(x, y) or self.has_q3_to_q1(x, y)) and \
            (self.has_q2_to_q4(x, y) or self.has_q4_to_q2(x, y))

    def get_part2(self):
        count = 0
        for y, row in enumerate(self.input):
            self.imit_x = len(row)
            for x, letter in enumerate(row):
                if self.middle == letter and self.is_valid_cross(x, y):
                    count += 1
        return count


aoc = AoCY2024D04()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

class AoCY2024D10:

    def __init__(self):
        self.input = self.get_input()
        self.limit_y = len(self.input)
        self.limit_x = len(self.input[0])

    def get_input(self):
        with open('inputs/10.txt') as file:
            return tuple(tuple(int(x) for x in line.strip()) for line in file)

    def try_path(self, num, x, y):
        target = num + 1
        total = 0
        if (x+1) < self.limit_x and self.input[y][x+1] == target:
            total += self.try_path(target, x+1, y)
        if (x-1) >= 0 and self.input[y][x-1] == target:
            total += self.try_path(target, x-1, y)
        if (y+1) < self.limit_y and self.input[y+1][x] == target:
            total += self.try_path(target, x, y+1)
        if (y-1) >= 0 and self.input[y-1][x] == target:
            total += self.try_path(target, x, y-1)
        return total

    def find_starts(self):
        scores = 0
        for y, row in enumerate(self.input):
            for x, num in enumerate(row):
                if 0 == num:
                    scores += self.try_path(num, x, y)
        return scores

    def get_part1(self):
        return self.find_starts()

    def get_part2(self):
        pass


aoc = AoCY2024D10()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

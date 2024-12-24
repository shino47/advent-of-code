class AoCY2024D10:

    def __init__(self):
        self.input = self.get_input()
        self.limit_y = len(self.input)
        self.limit_x = len(self.input[0])
        self.paths = []
        self.find_paths()

    def get_input(self):
        with open('inputs/10.txt') as file:
            return tuple(tuple(int(x) for x in line.strip()) for line in file)

    def try_path(self, num, x, y, path=None):
        if path is None:
            path = []
        else:
            path = list(path)
        path.append(f'{x},{y}')
        if 9 == num:
            self.paths.append(path)
            return
        target = num + 1
        if (x+1) < self.limit_x and self.input[y][x+1] == target:
            self.try_path(target, x+1, y, path)
        if (x-1) >= 0 and self.input[y][x-1] == target:
            self.try_path(target, x-1, y, path)
        if (y+1) < self.limit_y and self.input[y+1][x] == target:
            self.try_path(target, x, y+1, path)
        if (y-1) >= 0 and self.input[y-1][x] == target:
            self.try_path(target, x, y-1, path)

    def find_paths(self):
        for y, row in enumerate(self.input):
            for x, num in enumerate(row):
                if 0 == num:
                    self.try_path(num, x, y)

    def get_unique_paths(self):
        points = set()
        uniq = []
        for path in self.paths:
            point = (path[0], path[-1])
            if point not in points:
                points.add(point)
                uniq.append(path)
        return uniq

    def get_part1(self):
        return len(self.get_unique_paths())

    def get_part2(self):
        return len(self.paths)


aoc = AoCY2024D10()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

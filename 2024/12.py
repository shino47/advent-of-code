class AoCY2024D12:

    def __init__(self):
        self.input = self.get_input()
        self.limit_y = len(self.input)
        self.limit_x = len(self.input[0])
        self.marked = set()
        self.regions = self.get_regions()

    def get_input(self):
        with open('inputs/12.txt') as file:
            return tuple(tuple(x for x in line.strip()) for line in file)

    def find_region(self, char, x, y, region=None):
        if region is None:
            region = set()
        region.add((x, y))
        self.marked.add((x, y))
        if (x+1) < self.limit_x and self.input[y][x+1] == char and (x+1, y) not in self.marked:
            self.find_region(char, x+1, y, region)
        if (x-1) >= 0 and self.input[y][x-1] == char and (x-1, y) not in self.marked:
            self.find_region(char, x-1, y, region)
        if (y+1) < self.limit_y and self.input[y+1][x] == char and (x, y+1) not in self.marked:
            self.find_region(char, x, y+1, region)
        if (y-1) >= 0 and self.input[y-1][x] == char and (x, y-1) not in self.marked:
            self.find_region(char, x, y-1, region)
        return region

    def get_regions(self):
        regions = []
        for y, row in enumerate(self.input):
            for x, char in enumerate(row):
                if (x, y) in self.marked:
                    continue
                region = self.find_region(char, x, y)
                regions.append((char, region))
        return regions

    def get_perimeter(self, char, region):
        total = 0
        for x, y in region:
            if (x+1) >= self.limit_x or self.input[y][x+1] != char:
                total += 1
            if (x-1) < 0 or self.input[y][x-1] != char:
                total += 1
            if (y+1) >= self.limit_y or self.input[y+1][x] != char:
                total += 1
            if (y-1) < 0 or self.input[y-1][x] != char:
                total += 1
        return total

    def get_sides(self, char, region):
        total = 0
        for x, y in region:
            pass
        return total

    def get_part1(self):
        total = 0
        for char, region in self.regions:
            perimeter = self.get_perimeter(char, region)
            total += perimeter * len(region)
        return total

    def get_part2(self):
        total = 0
        for char, region in self.regions:
            sides = self.get_sides(char, region)
            total += sides * len(region)
        return total


aoc = AoCY2024D12()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

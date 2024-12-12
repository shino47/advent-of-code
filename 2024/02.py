class AoCY2024D02:

    def __init__(self):
        self.input = self.get_input()

    def get_input(self):
        with open('inputs/02.txt') as file:
            return tuple(tuple(line.split()) for line in file)

    def is_part1_safe(self, line):
        if line[0] == line[1]:
            return False
        is_increasing = int(line[1]) > int(line[0])
        prev = None
        for val in line:
            val = int(val)
            if prev is None:
                prev = val
                continue
            diff = (val - prev) if is_increasing else (prev - val)
            if diff > 3 or diff < 1:
                return False
            prev = val
        return True

    def get_part1(self):
        safes = 0
        for line in self.input:
            if self.is_part1_safe(line):
                safes += 1
        return safes

    def is_part2_valid(self, values):
        if values[0] == values[1]:
            return False
        is_increasing = int(values[1]) > int(values[0])
        prev = None
        for val in values:
            val = int(val)
            if prev is None:
                prev = val
                continue
            diff = (val - prev) if is_increasing else (prev - val)
            if diff > 3 or diff < 1:
                return False
            prev = val
        return True

    def is_part2_safe(self, line):
        if self.is_part2_valid(line):
            return True
        for idx, _ in enumerate(line):
            sublist = line[:idx] + line[idx + 1:]
            if self.is_part2_valid(sublist):
                return True
        return False

    def get_part2(self):
        safes = 0
        for line in self.input:
            if self.is_part2_safe(line):
                safes += 1
        return safes


aoc = AoCY2024D02()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

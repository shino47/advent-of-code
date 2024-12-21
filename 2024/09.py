class AoCY2024D09:

    def __init__(self):
        self.input = self.get_input()
        self.translation = self.get_translation()

    def get_input(self):
        with open('inputs/09.txt') as file:
            return tuple(int(elem) for elem in file.read().strip())

    def get_translation(self):
        items = []
        n = 0
        for i, num in enumerate(self.input):
            if i % 2 == 0:
                items += num * [n]
                n += 1
            else:
                items += num * ['.']
        return items

    def get_last_digit(self, values):
        for i, val in reversed(list(enumerate(values))):
            if val != '.':
                return i, val
        return None, None

    def get_reorder_by_block(self):
        values = self.translation
        for i, val in enumerate(values):
            if val != '.':
                continue
            x, num = self.get_last_digit(values)
            if x is None or x <= i:
                continue
            values[i] = num
            values[x] = val
        return values

    def get_checksum(self, values):
        total = 0
        for i, val in enumerate(values):
            if '.' != val:
                total += i * val
        return total

    def get_part1(self):
        ordered = self.get_reorder_by_block()
        return self.get_checksum(ordered)

    def get_part2(self):
        pass


aoc = AoCY2024D09()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

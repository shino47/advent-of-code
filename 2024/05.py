import math
from functools import cmp_to_key


class AoCY2024D05:

    def __init__(self):
        self.rules, self.updates = self.get_data()

    def get_data(self):
        with open('inputs/05.txt') as file:
            inp = file.read().split("\n\n")
            rules = {}
            for line in inp[0].split():
                values = [int(n) for n in line.split('|')]
                if values[0] not in rules:
                    rules[values[0]] = []
                rules[values[0]].append(values[1])
            updates = tuple(tuple(int(val) for val in line.strip().split(',')) for line in inp[1].split())
            return rules, updates

    def is_valid_before(self, values, num):
        for value in values:
            if value in self.rules[num]:
                return False
        return True

    def is_valid_after(self, values, num):
        for value in values:
            if value not in self.rules[num]:
                return False
        return True

    def is_valid(self, update):
        for idx, num in enumerate(update):
            if num not in self.rules:
                continue
            before = update[0:idx]
            after = update[idx + 1:]
            if not self.is_valid_after(after, num) or not self.is_valid_before(before, num):
                return False
        return True

    def get_middle_item(self, values):
        idx = math.floor(len(values) / 2)
        return values[idx]

    def compare(self, a, b):
        if a in self.rules and b in self.rules[a]:
            return -1
        elif b in self.rules and a in self.rules[b]:
            return 1
        return 0

    def get_fixed(self, values):
        return sorted(values, key=cmp_to_key(self.compare))

    def get_part1(self):
        items = []
        for update in self.updates:
            if self.is_valid(update):
                items.append(update)
        return sum([self.get_middle_item(item) for item in items])

    def get_part2(self):
        items = []
        for update in self.updates:
            if not self.is_valid(update):
                items.append(update)
        return sum([self.get_middle_item(self.get_fixed(item)) for item in items])


aoc = AoCY2024D05()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

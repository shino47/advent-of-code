import re


class AoCY2024D03:

    def __init__(self):
        self.input = self.get_input()

    def get_input(self):
        with open('inputs/03.txt') as file:
            return file.read()

    def get_part1(self):
        value = 0
        results = re.findall(r'mul\((\d{1,3})\,(\d{1,3})\)', self.input)
        for val1, val2 in results:
            value += int(val1) * int(val2)
        return value

    def get_part2(self):
        value = 0
        enabled = True
        results = re.findall(r"((?:do\(\)|don\'t\(\)).*?)?mul\((\d{1,3})\,(\d{1,3})\)", self.input)
        for action, val1, val2 in results:
            if action.startswith('do()'):
                enabled = True
            elif action.startswith("don't()"):
                enabled = False
            if enabled:
                value += int(val1) * int(val2)
        return value


aoc = AoCY2024D03()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

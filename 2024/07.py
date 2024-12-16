class AoCY2024D07:

    def __init__(self):
        self.input = self.get_input()
        self.operations = ('+', '*')

    def get_input(self):
        with open('inputs/07.txt') as file:
            values = []
            for line in file:
                parts = line.split(':')
                numbers = tuple(int(val) for val in parts[1].strip().split())
                values.append(tuple([int(parts[0]), numbers]))
            return tuple(values)

    def get_permutations(self, qty, current='', result=None):
        if result is None:
            result = []
        if len(current) == qty:
            result.append(current)
            return result
        for op in self.operations:
            self.get_permutations(qty, current + op, result)
        return result

    def merge_operations(self, values, permutations):
        result = []
        for perm in permutations:
            it = []
            for n, val in enumerate(values):
                it.append(val)
                if n < len(perm):
                    it.append(perm[n])
            result.append(it)
        return result

    def test_operations(self, target, operations):
        for op in operations:
            if self.calc_operation(op) == target:
                return True
        return False

    def calc_operation(self, operation):
        value = 0
        action = None
        for i, item in enumerate(operation):
            if 0 == i:
                value += item
                continue
            if item in self.operations:
                action = item
                continue
            if '+' == action:
                value += item
            else:
                value *= item
        return value

    def get_part1(self):
        total = 0
        for target, values in self.input:
            permutations = self.get_permutations(len(values) - 1)
            operations = self.merge_operations(values, permutations)
            if self.test_operations(target, operations):
                total += target
        return total


aoc = AoCY2024D07()
print('Answer 1:', aoc.get_part1())
# print('Answer 2:', aoc.get_part2())

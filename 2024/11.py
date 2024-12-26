class AoCY2024D11:

    def __init__(self):
        self.input = self.get_input()

    def get_input(self):
        with open('inputs/11.txt') as file:
            return [int(x) for x in file.read().strip().split()]

    def get_new_value(self, num):
        if 0 == num:
            return 1, None
        if len(str(num)) % 2 == 0:
            idx = len(str(num)) // 2
            return int(str(num)[:idx]), int(str(num)[idx:])
        return num * 2024, None

    def change(self, values):
        pending = []
        for key in list(values.keys()):
            qty = values[key]
            values[key] -= qty
            n1, n2 = self.get_new_value(key)
            if n1 in values:
                pending.append((n1, qty))
            else:
                values[n1] = values.get(n1, 0) + qty
            if n2 is None:
                continue
            if n2 in values:
                pending.append((n2, qty))
            else:
                values[n2] = values.get(n2, 0) + qty
        for num, qty in pending:
            values[num] = values.get(num, 0) + qty
        return {k: v for k, v in values.items() if v > 0}

    def blink(self, qty):
        dic = dict.fromkeys(list(self.input), 1)
        for _ in range(qty):
            dic = self.change(dic)
        return sum(dic.values())

    def get_part1(self):
        return self.blink(25)

    def get_part2(self):
        return self.blink(75)


aoc = AoCY2024D11()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

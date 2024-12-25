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
            half = len(str(num)) // 2
            n1 = int(str(num)[:half])
            n2 = int(str(num)[half:])
            return n1, n2
        return num * 2024, None

    def change(self, values):
        for key in list(values.keys()):
            qty = values[key]
            if qty <= 0:
                continue
            n1, n2 = self.get_new_value(key)
            values[n1] = values.get(n1, 0) + qty
            if n2 is not None:
                values[n2] = values.get(n2, 0) + qty
            values[key] -= qty
        return {k: v for k, v in values.items() if v > 0}

    def blink(self, qty):
        dic = dict.fromkeys(list(self.input), 1)
        print(dic)
        for _ in range(qty):
            dic = self.change(dic)
            print(_, dic)
            print(list(dic.keys()))
        return sum(dic.values())

    def get_part1(self):
        return self.blink(6)

    def get_part2(self):
        return self.blink(75)


aoc = AoCY2024D11()
print('Answer 1:', aoc.get_part1())
# print('Answer 2:', aoc.get_part2())

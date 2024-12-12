class AoCY2024D01:

    def __init__(self):
        self.list1, self.list2 = self.get_lists()

    def get_lists(self):
        with open('inputs/01.txt') as file:
            list1 = []
            list2 = []
            for line in file:
                x = line.split()
                list1.append(int(x[0]))
                list2.append(int(x[1]))
            return list1, list2

    def get_part1(self):
        data = []
        list1 = sorted(self.list1)
        list2 = sorted(self.list2)
        for idx, _ in enumerate(list1):
            val = abs(list1[idx] - list2[idx])
            data.append(val)
        return sum(data)

    def get_part2(self):
        data = []
        for val in self.list1:
            count = self.list2.count(val)
            data.append(val * count)
        return sum(data)


aoc = AoCY2024D01()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

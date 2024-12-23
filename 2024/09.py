class AoCY2024D09:

    def __init__(self):
        self.input = self.get_input()

    def get_input(self):
        with open('inputs/09.txt') as file:
            return tuple(int(elem) for elem in file.read().strip())

    def get_data(self):
        items = []
        n = 0
        for i, num in enumerate(self.input):
            is_pair = i % 2 == 0
            char = n if is_pair else None
            items.append((char, num))
            if is_pair:
                n += 1
        return items

    def get_flat_data(self, values):
        flat = []
        for item in values:
            flat += item[1] * [item[0]]
        return flat

    def get_checksum(self, values):
        total = 0
        for i, val in enumerate(values):
            if val is not None:
                total += i * val
        return total

    def get_last_digit(self, values):
        try:
            idx = len(values) - 1 - next(i for i, x in enumerate(reversed(values)) if x is not None)
            return idx
        except StopIteration:
            return None

    def get_reorder_by_item(self, values):
        for i, val in enumerate(values):
            if val is not None:
                continue
            x = self.get_last_digit(values)
            if x is None or x <= i:
                break
            values[i], values[x] = values[x], values[i]
        return values

    def get_first_free_index_of_size(self, values, idx, size):
        for i in range(len(values)):
            if i >= idx:
                break
            if values[i][0] is None and values[i][1] >= size:
                return i
        return None

    def move_block(self, values, idx_cur, idx_free):
        value = values[idx_cur][0]
        qty = values[idx_cur][1]
        remain_qty = values[idx_free][1] - qty
        values[idx_free] = (value, qty)
        values[idx_cur] = (None, qty)
        if remain_qty > 0:
            values.insert(idx_free + 1, (None, remain_qty))

    def get_reorder_by_block(self, values):
        for i in range(len(values) - 1, -1, -1):
            if values[i][0] is None:
                continue
            idx = self.get_first_free_index_of_size(values, i, values[i][1])
            if idx is not None:
                self.move_block(values, i, idx)
        return values

    def get_part1(self):
        data = self.get_data()
        flat = self.get_flat_data(data)
        ordered = self.get_reorder_by_item(flat)
        return self.get_checksum(ordered)

    def get_part2(self):
        data = self.get_data()
        ordered = self.get_reorder_by_block(data)
        flat = self.get_flat_data(ordered)
        return self.get_checksum(flat)


aoc = AoCY2024D09()
print('Answer 1:', aoc.get_part1())
print('Answer 2:', aoc.get_part2())

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
            if 0 == num:
                continue
            is_pair = i % 2 == 0
            char = n if is_pair else '.'
            items.append({
                'value': char,
                'qty': num,
            })
            if is_pair:
                n += 1
        return items

    def get_flat_data(self, values):
        flat = []
        for item in values:
            flat += item['qty'] * [item['value']]
        return flat

    def get_checksum(self, values):
        total = 0
        for i, val in enumerate(values):
            if '.' != val:
                total += i * val
        return total

    def get_last_digit(self, values):
        for i, val in reversed(list(enumerate(values))):
            if '.' != val:
                return i, val
        return None, None

    def get_reorder_by_item(self, values):
        for i, val in enumerate(values):
            if '.' != val:
                continue
            x, num = self.get_last_digit(values)
            if x is None or x <= i:
                continue
            values[i] = num
            values[x] = val
        return values

    def get_first_free_index_of_size(self, values, idx, size):
        for i in range(len(values)):
            if i >= idx:
                break
            if '.' == values[i]['value'] and values[i]['qty'] >= size:
                return i
        return None

    def move_block(self, values, idx_cur, idx_free):
        value = values[idx_cur]['value']
        qty = values[idx_cur]['qty']
        remain_qty = values[idx_free]['qty'] - qty
        values[idx_free] = {
            'value': value,
            'qty': qty,
        }
        values[idx_cur] = {
            'value': '.',
            'qty': qty,
        }
        if remain_qty > 0:
            values.insert(idx_free + 1, {
                'value': '.',
                'qty': remain_qty,
            })

    def get_reorder_by_block(self, values):
        for i in range(len(values) - 1, -1, -1):
            if '.' == values[i]['value']:
                continue
            idx = self.get_first_free_index_of_size(values, i, values[i]['qty'])
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

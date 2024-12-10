def has_south_east(data, x, y):
    return 'M' == data[y - 1][x - 1] and 'S' == data[y + 1][x + 1]


def has_south_west(data, x, y):
    return 'M' == data[y - 1][x + 1] and 'S' == data[y + 1][x - 1]


def has_north_east(data, x, y):
    return 'M' == data[y + 1][x - 1] and 'S' == data[y - 1][x + 1]


def has_north_west(data, x, y):
    return 'M' == data[y + 1][x + 1] and 'S' == data[y - 1][x - 1]


def is_valid(data, x, y, limit_x, limit_y):
    if (x - 1) < 0 or (y - 1) < 0 or (x + 1) >= limit_x or (y + 1) >= limit_y:
        return False
    return (has_south_east(data, x, y) or has_north_west(data, x, y)) and \
        (has_south_west(data, x, y) or has_north_east(data, x, y))


with open('input.txt') as file:
    count = 0
    data = tuple(tuple(line.strip()) for line in file)
    limit_y = len(data)
    for y, row in enumerate(data):
        limit_x = len(row)
        for x, letter in enumerate(row):
            if 'A' == letter and is_valid(data, x, y, limit_x, limit_y):
                count += 1
    print(count)

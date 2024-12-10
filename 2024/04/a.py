def has_east(data, key, x, y, limit_x):
    if (len(key) + x) > limit_x:
        return False
    for n, letter in enumerate(key):
        if data[y][x + n] != letter:
            return False
    return True


def has_south(data, key, x, y, limit_y):
    if (len(key) + y) > limit_y:
        return False
    for n, letter in enumerate(key):
        if data[y + n][x] != letter:
            return False
    return True


def has_west(data, key, x, y):
    if (x - len(key) + 1) < 0:
        return False
    for n, letter in enumerate(key):
        if data[y][x - n] != letter:
            return False
    return True


def has_north(data, key, x, y):
    if (y - len(key) + 1) < 0:
        return False
    for n, letter in enumerate(key):
        if data[y - n][x] != letter:
            return False
    return True


def has_south_east(data, key, x, y, limit_x, limit_y):
    if (len(key) + x) > limit_x or (len(key) + y) > limit_y:
        return False
    for n, letter in enumerate(key):
        if data[y + n][x + n] != letter:
            return False
    return True


def has_south_west(data, key, x, y, limit_y):
    if (x - len(key) + 1) < 0 or (len(key) + y) > limit_y:
        return False
    for n, letter in enumerate(key):
        if data[y + n][x - n] != letter:
            return False
    return True


def has_north_east(data, key, x, y, limit_x):
    if (len(key) + x) > limit_x or (y - len(key) + 1) < 0:
        return False
    for n, letter in enumerate(key):
        if data[y - n][x + n] != letter:
            return False
    return True


def has_north_west(data, key, x, y):
    if (x - len(key) + 1) < 0 or (y - len(key) + 1) < 0:
        return False
    for n, letter in enumerate(key):
        if data[y - n][x - n] != letter:
            return False
    return True


def get_qty(data, key, x, y, limit_x, limit_y):
    values = [
        has_east(data, key, x, y, limit_x),
        has_south(data, key, x, y, limit_y),
        has_west(data, key, x, y),
        has_north(data, key, x, y),
        has_south_east(data, key, x, y, limit_x, limit_y),
        has_south_west(data, key, x, y, limit_y),
        has_north_east(data, key, x, y, limit_x),
        has_north_west(data, key, x, y),
    ]
    return len([valid for valid in values if valid])


with open('input.txt') as file:
    key = ('X', 'M', 'A', 'S')
    count = 0
    data = tuple(tuple(line.strip()) for line in file)
    limit_y = len(data)
    for y, row in enumerate(data):
        limit_x = len(row)
        for x, letter in enumerate(row):
            if key[0] == letter:
                count += get_qty(data, key, x, y, limit_x, limit_y)
    print(count)

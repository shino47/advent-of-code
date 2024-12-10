def has_east(data, x, y, limit_x, limit_y):
    pass


def has_south(data, x, y, limit_x, limit_y):
    pass


def has_west(data, x, y, limit_x, limit_y):
    pass


def has_north(data, x, y, limit_x, limit_y):
    pass


def has_south_east(data, x, y, limit_x, limit_y):
    pass


def has_south_west(data, x, y, limit_x, limit_y):
    pass


def has_north_east(data, x, y, limit_x, limit_y):
    pass


def has_north_west(data, x, y, limit_x, limit_y):
    pass


def has_found(data, x, y, limit_x, limit_y):
    return has_east(data, x, y, limit_x, limit_y) \
        and has_south(data, x, y, limit_x, limit_y) \
        and has_west(data, x, y, limit_x, limit_y) \
        and has_north(data, x, y, limit_x, limit_y) \
        and has_south_east(data, x, y, limit_x, limit_y) \
        and has_south_west(data, x, y, limit_x, limit_y) \
        and has_north_east(data, x, y, limit_x, limit_y) \
        and has_north_west(data, x, y, limit_x, limit_y)


with open('input.txt') as file:
    count = 0
    data = tuple(tuple(line.strip()) for line in file)
    limit_y = len(data)
    for y, row in enumerate(data):
        limit_x = len(row)
        for x, letter in enumerate(row):
            if 'X' == letter and has_found(data, x, y, limit_x, limit_y):
                count += 1
    print(count)

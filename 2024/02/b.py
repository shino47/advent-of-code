def is_valid(values):
    if values[0] == values[1]:
        return False
    is_increasing = int(values[1]) > int(values[0])
    prev = None
    for val in values:
        val = int(val)
        if prev is None:
            prev = val
            continue
        diff = (val - prev) if is_increasing else (prev - val)
        if diff > 3 or diff < 1:
            return False
        prev = val
    return True


def is_safe(line):
    values = line.split()
    if is_valid(values):
        return True
    for idx, _ in enumerate(values):
        sublist = values[:idx] + values[idx + 1:]
        if is_valid(sublist):
            return True
    return False


with open('input.txt') as file:
    safes = 0
    for line in file:
        if is_safe(line):
            safes += 1
    print(safes)

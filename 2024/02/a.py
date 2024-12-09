list1 = []
list2 = []
safes = 0


def is_safe(line):
    values = line.split()
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


with open('input.txt') as file:
    for line in file:
        if is_safe(line):
            safes += 1
    print(safes)

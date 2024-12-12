def get_rules(content):
    data = {}
    for line in content.split():
        values = [int(n) for n in line.split('|')]
        if not values[0] in data:
            data[values[0]] = []
        data[values[0]].append(values[1])
    return data


def is_valid(update, rules):
    for idx, num in enumerate(update):
        before = update[0:idx]
        after = update[idx + 1:]
    return True


with open('input.txt') as file:
    data = file.read().split("\n\n")
    rules = get_rules(data[0])
    updates = tuple(tuple(int(val) for val in line.strip().split(',')) for line in data[1].split())
    for update in updates:
        if is_valid(update, rules):
            print(update)

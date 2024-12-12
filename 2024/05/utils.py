import math
from functools import partial, cmp_to_key


def get_rules(content):
    data = {}
    for line in content.split():
        values = [int(n) for n in line.split('|')]
        if values[0] not in data:
            data[values[0]] = []
        data[values[0]].append(values[1])
    return data


def get_data():
    with open('input.txt') as file:
        data = file.read().split("\n\n")
        rules = get_rules(data[0])
        updates = tuple(tuple(int(val) for val in line.strip().split(',')) for line in data[1].split())
        return rules, updates


def is_valid_before(values, num, rules):
    for value in values:
        if value in rules[num]:
            return False
    return True


def is_valid_after(values, num, rules):
    for value in values:
        if value not in rules[num]:
            return False
    return True


def is_valid(update, rules):
    for idx, num in enumerate(update):
        if num not in rules:
            continue
        before = update[0:idx]
        after = update[idx + 1:]
        if not is_valid_after(after, num, rules) or not is_valid_before(before, num, rules):
            return False
    return True


def get_middle_item(values):
    idx = math.floor(len(values) / 2)
    return values[idx]


def compare(rules, a, b):
    if a in rules and b in rules[a]:
        return -1
    elif b in rules and a in rules[b]:
        return 1
    return 0


def get_fixed(values, rules):
    comp = partial(compare, rules)
    return sorted(values, key=cmp_to_key(comp))

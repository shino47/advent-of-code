import re


with open('input.txt', 'r') as file:
    value = 0
    mult = True
    results = re.findall(r"((?:do\(\)|don\'t\(\)).*?)?mul\((\d{1,3})\,(\d{1,3})\)", file.read())
    for action, val1, val2 in results:
        if action.startswith('do()'):
            mult = True
        elif action.startswith("don't()"):
            mult = False
        if mult:
            value += int(val1) * int(val2)
    print(value)

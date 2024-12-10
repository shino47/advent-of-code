import re


with open('input.txt', 'r') as file:
    value = 0
    results = re.findall(r'mul\((\d{1,3})\,(\d{1,3})\)', file.read())
    for val1, val2 in results:
        value += int(val1) * int(val2)
    print(value)

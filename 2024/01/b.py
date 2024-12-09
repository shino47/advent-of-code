list1 = []
list2 = []
data = []

with open('input.txt') as file:
    for line in file:
        x = line.split()
        list1.append(int(x[0]))
        list2.append(int(x[1]))
    for val in list1:
        count = list2.count(val)
        data.append(val * count)
    print(sum(data))

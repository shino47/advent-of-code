with open('input.txt') as file:
    list1 = []
    list2 = []
    data = []
    for line in file:
        x = line.split()
        list1.append(int(x[0]))
        list2.append(int(x[1]))
    list1.sort()
    list2.sort()
    for idx, _ in enumerate(list1):
        val = abs(list1[idx] - list2[idx])
        data.append(val)
    print(sum(data))

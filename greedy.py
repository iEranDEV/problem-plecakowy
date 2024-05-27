def greedy(n, c, items):
    factor = []
    for index, item in enumerate(items):
        factor.append((index, item[1] / item[0]))
    sorted_factor = sorted(factor, key=lambda x: x[1], reverse=True)

    elements = []

    count = 1
    value = 0
    waga = 0

    for i in sorted_factor:
        if count <= n and waga + items[i[0]][0] <= c:
            value += items[i[0]][1]
            waga += items[i[0]][0]
            count += 1
            elements.append(i[0])

    return [waga, value, elements]

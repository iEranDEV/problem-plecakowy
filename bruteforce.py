def bruteforce(n, c, items):
    fmax = 0
    rozmiar = 0
    elements = []

    for i in range(1, pow(2,  n)):
        binary = "{0:b}".format(i)
        w = 0
        for index, value in enumerate(binary[::-1]):
            if value == '1':
                w += items[index][0]
        if w <= c:
            f = 0
            for index, value in enumerate(binary[::-1]):
                if value == '1':
                    f += items[index][1]
            if f > fmax:
                fmax = f
                rozmiar = w
                elements = []
                for index, value in enumerate(binary[::-1]):
                    if value == '1':
                        elements.append(1)
                    else:
                        elements.append(0)

    return [rozmiar, fmax, elements]

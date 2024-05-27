def dynamic(n, c, items):
    matrix = []
    fmax = 0
    waga = 0
    elements = [0 for _ in range(n)]

    for i in range(n + 1):
        matrix.append([0 for _ in range(c + 1)])
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if items[i - 1][0] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - items[i - 1][0]] + items[i - 1][1])

    current = [n, c]
    fmax = matrix[current[0]][current[1]]
    while matrix[current[0]][current[1]] != 0:
        if matrix[current[0]][current[1]] == matrix[current[0] - 1][current[1]]:
            current = [current[0] - 1, current[1]]
        elif matrix[current[0]][current[1]] > matrix[current[0] - 1][current[1]]:
            elements[current[0] - 1] = 1
            waga += items[current[0] - 1][0]
            current = [current[0] - 1, current[1] - items[current[0] - 1][0]]

    return [waga, fmax, elements]

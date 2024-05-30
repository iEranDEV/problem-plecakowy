import random
import timeit
from bruteforce import bruteforce
from greedy import greedy
from dynamic import dynamic


def generate_knapsack_data(n, min_size, max_size, min_value, max_value):
    items = []
    for i in range(0, n):
        size = random.randint(min_size, max_size)
        value = random.randint(min_value, max_value)
        items.append([size, value])

    return items


itemsCount = [10, 20, 40, 250]
capacities = [10, 20, 40, 250]

for n in itemsCount:
    items = generate_knapsack_data(n, 1, 20, 1, 100)
    print(f'n = {n}')
    for b in capacities:
        print(f'    b = {b}')

        # AD
        start_0 = timeit.default_timer()
        dynamic(n, b, items)
        end_0 = timeit.default_timer()
        print('        AD = {:.10f}'.format(end_0 - start_0).replace(".", ","))

        # AZ
        start_1 = timeit.default_timer()
        greedy(n, b, items)
        end_1 = timeit.default_timer()
        print('        AZ = {:.10f}'.format(end_1 - start_1).replace(".", ","))

        # AB
        start_2 = timeit.default_timer()
        bruteforce(n, b, items)
        end_2 = timeit.default_timer()
        print('        AB = {:.10f}'.format(end_2 - start_2).replace(".", ","))

import utils
from bruteforce import bruteforce
from greedy import greedy
from dynamic import dynamic

n = 0
c = 0
items = []

readFile = open("input.txt", "r")
for index, line in enumerate(readFile):
    if index == 0:
        n, c = list(map(int, line.rstrip('\n').split()))
    else:
        items.append(list(map(int, line.rstrip('\n').split())))
readFile.close()

utils.menu("Jaki typ algorytmu?", ["Programowania dynamicznego", "Algorytm zachłanny", "Algorytm siłowy"])
inputType = int(input("Podaj typ algorytmu: "))

if inputType == 1:
    rozmiar, value, elements = dynamic(n, c, items)
    print(f'Rozmiar = {rozmiar}')
    print(f'Wartość = {value}')
    print("Przedmioty:", end=" ")
    for i in range(0, len(items)):
        if elements[i] == 1:
            print(i + 1, end=" ")
elif inputType == 2:
    rozmiar, value, elements = greedy(n, c, items)
    print(f'Rozmiar = {rozmiar}')
    print(f'Wartość = {value}')
    print("Przedmioty:", end=" ")
    for index, _ in enumerate(items):
        if index in elements:
            print(index + 1, end=" ")
elif inputType == 3:
    rozmiar, value, elements = bruteforce(n, c, items)
    print(f'Rozmiar = {rozmiar}')
    print(f'Wartość = {value}')
    print("Przedmioty:", end=" ")
    for i in range(0, len(items)):
        if elements[i] == 1:
            print(i + 1, end=" ")

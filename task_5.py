from functools import reduce

print(reduce(lambda el_1, el_2: el_1 * el_2, list(range(100, 1001, 2))))

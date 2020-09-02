my_list = [1, 1.5, "some words", True, [1, 3], (1, 5), {4, 5}, {'key_1': 2, 54: 3}]
n = 1
n2 = 0

for elem in my_list:
    print(f"{n}. {my_list[n2]} - {type(elem)}")
    n += 1
    n2 += 1

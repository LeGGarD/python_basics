strings = input("Введите набор слов через пробел:  ")

for ind, el in enumerate(strings.split(), 1):
    if len(el) > 10:
        print(ind, el[0:10])
    else:
        print(ind, el)

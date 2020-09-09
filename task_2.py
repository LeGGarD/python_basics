from random import randrange

my_list = []

while len(my_list) < 10:
    my_list.append(randrange(0, 101))

new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]

print(f"Вот сгенерированный список: {my_list}"
      f"\nА вот отсортированный: {new_list}")

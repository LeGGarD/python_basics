from random import randrange

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
rand_list = []

while len(rand_list) < 30:
    rand_list.append(randrange(0, 50))

print(f"Список из примера:\n{my_list}\nРандомно-сгенерированный список:\n{rand_list}\n{'- ' * 64}"
      f"\nРешаем первым методом\n{'- ' * 64}")
# first solution
print(
    f"Первый список без дублей:"
    f"\n{[my_list[el] for el in range(len(my_list)) if my_list[el] not in my_list[0: el] and my_list[el] not in my_list[el + 1: len(my_list)]]}"
    f"\nВторой список без дублей:"
    f"\n{[rand_list[el] for el in range(len(rand_list)) if rand_list[el] not in rand_list[0: el] and rand_list[el] not in rand_list[el + 1: len(rand_list)]]}")
# second solution
print(f"{'- ' * 64}\nТеперь решаем вторым методом\n{'- ' * 64}\nПервый список без дублей:"
      f"\n{[my_list[i] for i in range(len(my_list)) if my_list.count(my_list[i]) == 1]}"
      f"\nВторой список без дублей:"
      f"\n{[rand_list[i] for i in range(len(rand_list)) if rand_list.count(rand_list[i]) == 1]}")

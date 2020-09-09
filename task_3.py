my_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]

print(f"Все числа в диапазоне от 20 до 240, которые целочисленно делятся на 20 И 21:"
      f"\n{my_list}")

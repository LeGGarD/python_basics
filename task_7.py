def fact(quantity):
    for el in list(range(1, quantity + 1)):
        yield el


fact_val = 1
a_string = ""
try:
    for el in fact(int(input("Введите факториал числа (целое натуральное): "))):
        fact_val *= el
        a_string = a_string + " * " + str(el)

    print(f"{a_string[3:len(a_string)]} = {fact_val}")
except ValueError:
    print("Введено неправильное число")

from sys import argv
try:
    name, hours, rate, award = argv
except ValueError:
    print("You entered more/less values, than you had to")
    quit()


def income_func():
    try:
        global hours, rate, award
        return int(hours) * int(rate) + int(award)
    except ValueError:
        print("Try to enter only numbers, as parameters")


print(f"Введенные параметры: {argv[1: len(argv)]}"
      f"\nЗаработная плата по введенным параметрам состовляет: {income_func()}")

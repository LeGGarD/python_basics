def my_func(x=0, y=0):
    """Функция возведения в отрицательную степень

    :param x: любое действительное положительное число
    :param y: степень, в которую возводится число
    :return: результат преобразования
    """
    try:
        x = abs(float(input("Введите действительное положительное число: ")))
        y = abs(int(input("Введите целое отрицательное число: ")))
        mult_val = 1
    except ValueError:
        print("Ошибка. Введены некорректные символы")
    try:
        while y > 0:
            mult_val *= x
            y -= 1
        fin_val = 1 / mult_val
        return fin_val
    except ZeroDivisionError:
        print("Ошибка деления на ноль")


try:
    print(f"{float(my_func()):.5f}")
except TypeError:
    print("Ошибка ввода. Невозможно вывести финальный расчет :(")
except UnboundLocalError:
    print("Ошбика ввода. Вы ввели НЕ числа")

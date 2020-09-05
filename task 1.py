def div_func(s_1=0, s_2=0):
    """Простейшая функция деления

    :return: результат деления
    """
    s_1 = int(input("Введите первое число: "))
    s_2 = int(input("Введите второе число: "))
    try:
        div_val = s_1 / s_2
        return div_val
    except ZeroDivisionError:
        print("Нельзя делить на ноль")


div_func_val = div_func()
print(div_func_val)

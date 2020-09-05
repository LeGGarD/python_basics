def my_func(s_1=0, s_2=0, s_3=0):
    """Функция для расчета суммы двух больших переменных

    :param s_1: переменная 1
    :param s_2: переменная 2
    :param s_3: переменная 3
    :return: результат расчетов
    """
    try:
        s_1 = int(input("Введите первое число: "))
        s_2 = int(input("Введите второе число: "))
        s_3 = int(input("Введите третье число: "))
        a_list = [s_1, s_2, s_3]
        a_list.remove(min(a_list))
        a_sum = a_list[0] + a_list[1]
        return a_sum
    except ValueError:
        print("Для рачетов необходимо вводить только числа")


my_func_val = my_func()
print(my_func_val)

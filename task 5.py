a_sum = 0

while True:
    def my_func():
        """Функция суммирования нескольких чисел, введенных через пробел

        :return: сумма всех введенных чисел
        """
        global a_sum
        arg_list = input("Введите набор чисел через пробел, либо напишите 'q' для выхода: ").split()
        try:
            for el in arg_list:
                if el == "q".lower():
                    print(f"{64 * '-'}\nВот ваша финальная сумма: {a_sum}")
                    quit()
                else:
                    a_sum += int(el)
            return a_sum
        except ValueError:
            print(f"{64 * '-'}\nВНИМАНИЕ! Введен неправильный символ для выхода (или случайный ввод)\n{64 * '-'}")


    my_func_val = my_func()
    print(f"{64 * '-'}\nВот ваша сумма: {a_sum}")

def user_info(name=None, surname=None, birth_year=None, city=None, email=None, phone_num=None):
    """Функция вывода данных пользователя

    :param name: имя
    :param surname: фамилия
    :param birth_year: год рождения
    :param city: город проживания
    :param email: имейл
    :param phone_num: телефон
    :return: строка, содержащая все данные сразу
    """
    name = input("Введите свое имя: ").title()
    surname = input("Введите свою фамилию: ").title()
    birth_year = input("Введите свой год рождения: ")
    city = input("Введите свой город проживания: ").title()
    email = input("Введите свой email: ")
    phone_num = input("Введите свой телефон: ")
    print(f"name - {name}, surname - {surname}, birth_year - {birth_year}, city - {city}, email - {email}, "
          f"phone_num - {phone_num}")


print(user_info())

class NewError(Exception):
    def __init__(self, txt):
        self.txt = txt


def isfloat(str_):
    try:
        float(str_)
    except ValueError:
        print("You have to input only numbers!")
    return True

l = []
while True:
    s = input("Введите числа через пробел или q для выхода: ").split()
    if "q" in s:
        print(l)
        break
    for el in s:
        try:
            if el.isdigit() is not True and el.replace('.', "1").isdigit() is not True:
                raise NewError("You can only enter numbers")
            else:
                l.append(el)
        except NewError as err:
            print(err)

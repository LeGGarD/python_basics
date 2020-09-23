class NewError(Exception):
    def __init__(self, txt):
        self.txt = txt


i1 = int(input("Enter the first number: "))
i2 = int(input("Enter the second number: "))

try:
    if i2 is 0:
        raise NewError("You can't divide nums by zero!")
    i = i1 / i2
except NewError as err:
    print(err)
else:
    print(i)


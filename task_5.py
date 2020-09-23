class ComplNum:
    def __init__(self, c):
        self.c = c

    def __add__(self, other):
        r_p = self.c.real + other.c.real
        i_p = self.c.imag + other.c.imag
        return complex(r_p, i_p)

    def __mul__(self, other):
        r_p = self.c.real * other.c.real - self.c.imag * other.c.imag
        i_p = self.c.real * other.c.imag + other.c.real * self.c.imag
        return complex(r_p, i_p)


first = ComplNum(2 + 5j)
second = ComplNum(3 + 4j)
print(first + second)
print(first * second)

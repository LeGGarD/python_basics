class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        _sub = self.quantity - other.quantity
        if _sub >= 0:
            return self.quantity - other.quantity
        else:
            print("Нельзя вычетать из меньшего большее.")

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __floordiv__(self, other):
        return round(self.quantity / other.quantity)

    def make_order(self, a_quantity, rows):
        _str = f"{a_quantity * '*'}"
        n_str = ""
        n = 0
        for el in _str:
            n += 1
            if n <= rows:
                n_str += el
            else:
                n_str += f"\n{el}"
                n = 1
        return n_str


cell_1 = Cell(15)
cell_2 = Cell(3)

print(f"Если сложить клетки, их будет: {cell_1 + cell_2}\nЭто вот столько:\n{cell_1.make_order(cell_1 + cell_2, 15)}\n")

if cell_1.__sub__(cell_2) is not None:
    print(
        f"Если вычесть клетки, их будет: {cell_1 - cell_2}\nЭто вот столько:\n{cell_1.make_order(cell_1 - cell_2, 15)}\n")
else:
    print()

print(
    f"Если умножить клетки, их будет: {cell_1 * cell_2}\nЭто вот столько:\n{cell_1.make_order(cell_1 * cell_2, 15)}\n")

print(
    f"Если разделить клетки, их будет: {cell_1 // cell_2}\nЭто вот столько:\n{cell_1.make_order(cell_1 // cell_2, 15)}\n")

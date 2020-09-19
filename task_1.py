import random


def matrix_generator(rows, columns):
    main_list = []
    for i in range(rows):
        main_list.append([random.randint(1, 65323) for i in range(columns)])
    return main_list


class Matrix:
    def __init__(self, rand_matrix):
        self.rand_matrix = rand_matrix

    def __add__(self, other):
        result = []
        for sublist in zip(self.rand_matrix, other.rand_matrix):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            result.append(temp)
        fin = ""
        for el in result:
            fin += f"{el}\n"
        return fin

    def __str__(self):
        fin = ""
        for el in self.rand_matrix:
            fin += f"{el}\n"
        return fin


matrix_1 = Matrix(matrix_generator(2, 3))
matrix_2 = Matrix(matrix_generator(2, 3))

print(f"Вот первая матрица\n{matrix_1}")
print(f"Вот вторая матрица\n{matrix_2}")

print(f"Вот сумма матриц\n{matrix_1 + matrix_2}")

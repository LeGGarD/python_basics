class Road:

    def mass_count(self, _length, _width):
        print(f"Масса дорожного полотна по заданным параметрам:\n"
              f"{_length}м * {_width}м * 25кг * 5см = {int(_length) * int(_width) * 25 * 5 //1000}т")


result = Road()
result.mass_count(20, 5000)

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen:

    def __init__(self, title):
        Stationery.title = title

    def draw(self):
        print("Рисуем ручкой")


class Pencil:

    def __init__(self, title):
        Stationery.title = title

    def draw(self):
        print("Рисуем карандашом")


class Handle:

    def __init__(self, title):
        Stationery.title = title

    def draw(self):
        print("Рисуем маркером")


stationary = Stationery("Загрузка")
stationary.draw()

pen = Pen("Ручка")
pen.draw()

pencil = Pencil("Карандаш")
pencil.draw()

handle = Handle("Маркер")
handle.draw()

from abc import abstractmethod
import random


class Clothes:
    @abstractmethod
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def cloth_needed(self):
        pass


class Coat(Clothes):
    def __init__(self, title, v):
        super().__init__(title)
        self.v = v

    @property
    def cloth_needed(self):
        return f"Для пально необходимо: {self.v / 6.5 + 0.5} ткани"


class Costume(Clothes):
    def __init__(self, title, h):
        super().__init__(title)
        self.h = h

    @property
    def cloth_needed(self):
        return f"Для костюма необходимо: {2 * self.h + 0.3} ткани"


coat = Coat("Пальто", random.randrange(50, 80))
print(coat.cloth_needed)

costume = Costume("Костюм", random.randrange(150, 200))
print(costume.cloth_needed)

class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):

    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


sample = Position("Vasiliy", "Goloborod'ko", "Project Manager", {"wage": 80000, "bonus": 15000})
print(f"Работник: {sample.get_full_name()}")
print(f"Его зар. плата с учетом бонуса: {sample.get_total_income()}")

"""В этом варианте решения, подразделения компании выражены тремя, наследующими класс Company, классами
Поэтому тут много статик-методов и нет ни одного объекта.

Еще, тут по большому счету бесполезны 3 переменные, printers/scaners/xeroxes -
это задел на какие-то будущие реализации этих переменных :)

Все основные действия происходят через класс Storage.
Можно добавлять на него технику и перераспределять её по подразделениям компании
"""
from abc import abstractmethod


class Company:
    stationery = {"printers": 0, "scaners": 0, "xeroxes": 0}
    printers = 0
    scaners = 0
    xeroxes = 0

    @staticmethod
    def info():
        print(f"Company now owns: {Company.stationery}")


class Bookkeeping(Company):
    stationery = {"printers": 0, "scaners": 0, "xeroxes": 0}
    printers = 0
    scaners = 0
    xeroxes = 0

    @staticmethod
    def info():
        print(f"Bookkeeping now owns: {Bookkeeping.stationery}")


class HumanResourcesDepartment(Company):
    stationery = {"printers": 0, "scaners": 0, "xeroxes": 0}
    printers = 0
    scaners = 0
    xeroxes = 0

    @staticmethod
    def info():
        print(f"HR Department now owns: {HumanResourcesDepartment.stationery}")


class MainOffice(Company):
    stationery = {"printers": 0, "scaners": 0, "xeroxes": 0}
    printers = 0
    scaners = 0
    xeroxes = 0

    @staticmethod
    def info():
        print(f"Main Office now owns: {MainOffice.stationery}")


class Storage(Company):
    stationery = {"printers": 0, "scaners": 0, "xeroxes": 0}
    printers = 0
    scaners = 0
    xeroxes = 0

    @classmethod
    def add_tech(cls, tech_type, quantity):
        if tech_type == "Printer":
            Storage.stationery["printers"] += quantity
            Company.stationery["printers"] += quantity
            Storage.printers += 1
            Company.printers += 1
        elif tech_type == "Scaner":
            Storage.stationery["scaners"] += quantity
            Company.stationery["scaners"] += quantity
            Storage.scaners += 1
            Company.scaners += 1
        elif tech_type == "Xerox":
            Storage.stationery["xeroxes"] += quantity
            Company.stationery["xeroxes"] += quantity
            Storage.xeroxes += 1
            Company.xeroxes += 1
        else:
            print("You wrote wrong 'tech_type'!")

    @staticmethod
    def info():
        print(f"Storage now contains: {Storage.stationery}")

    @classmethod
    def tech_distribute(cls, tech_type, destination, quantity):
        if tech_type == "Printer":
            Storage.stationery["printers"] -= quantity
            destination.stationery["printers"] += quantity
            Storage.printers -= 1
            destination.printers += 1
        elif tech_type == "Scaner":
            Storage.stationery["scaners"] -= quantity
            destination.stationery["scaners"] += quantity
            Storage.scaners -= 1
            destination.scaners += 1
        elif tech_type == "Xerox":
            Storage.stationery["xeroxes"] -= quantity
            destination.stationery["xeroxes"] += quantity
            Storage.xeroxes -= 1
            destination.xeroxes += 1
        else:
            print("You wrote wrong 'tech_type'!")


class Stationery:
    @abstractmethod
    def __init__(self, title):
        self.title = title


class Printer(Stationery):
    def __init__(self, title, fill_status):
        super().__init__(title)
        self.fill_status = fill_status


class Scaner(Stationery):
    def __init__(self, title, scan_speed):
        super().__init__(title)
        self.scan_speed = scan_speed


class Xerox(Stationery):
    def __init__(self, title, capacity):
        super().__init__(title)
        self.capacity = capacity


p = Printer("Printer", "Status: full")
s = Scaner("Scaner", 15)
x = Xerox("Xerox", 100)

Company.info()
print()

print(f"{36 * '* '}\nCompany purchases some stationery ...\n{36 * '* '}")
Storage.add_tech("Printer", 1)
Storage.add_tech("Xerox", 5)
Storage.add_tech("Scaner", 3)
Company.info()
Storage.info()
print()

print(f"{36 * '* '}\nThe company decided to distribute some stationery from the storage\n{36 * '* '}")
Storage.tech_distribute("Printer", Bookkeeping, 1)
Storage.tech_distribute("Xerox", Bookkeeping, 1)
Storage.tech_distribute("Scaner", Bookkeeping, 1)
Storage.tech_distribute("Xerox", HumanResourcesDepartment, 1)
Storage.tech_distribute("Scaner", HumanResourcesDepartment, 1)
Storage.tech_distribute("Xerox", MainOffice, 2)
Storage.tech_distribute("Scaner", MainOffice, 1)
Company.info()
Storage.info()
MainOffice.info()
HumanResourcesDepartment.info()
Bookkeeping.info()

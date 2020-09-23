"""В этом варианте решения, 3 подразделения компании выражены тремя объектами класса Company
Это значительно экономит место и убирает тавтологию переменных.

Но как по мне, первый вариант более интересный, так как я представляю 3 подразделения компании,
наполненные абсолютно разными, собственными объектами, чтобы в каждом подразделении были свои методы и тд.

На написания настолько детального задания у меня сейчас не хватало времени и сил, но в целом, такая идея)
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

    def __init__(self, title, printers, scaners, xeroxes):
        self.title = title
        self.printers = printers
        self.scaners = scaners
        self.xeroxes = xeroxes

    def __str__(self):
        print(f"{self.title} now owns: {self.printers} printers, {self.scaners} scaners, {self.scaners} scaners,")


class Storage(Company):
    stationery = {"printers": 0, "scaners": 0, "xeroxes": 0}
    printers = 0
    scaners = 0
    xeroxes = 0

    @classmethod
    def add_tech(cls, tech_type, quantity):
        if tech_type == p.title:
            Storage.stationery["printers"] += quantity
            Company.stationery["printers"] += quantity
            Storage.printers += 1
            Company.printers += 1
        elif tech_type == s.title:
            Storage.stationery["scaners"] += quantity
            Company.stationery["scaners"] += quantity
            Storage.scaners += 1
            Company.scaners += 1
        elif tech_type == x.title:
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
    def tech_distribute(cls, tech_type, quantity, destination):
        if tech_type == p.title:
            Storage.stationery["printers"] -= quantity
            Storage.printers -= quantity
            destination.printers += quantity
        elif tech_type == s.title:
            Storage.stationery["scaners"] -= quantity
            Storage.scaners -= quantity
            destination.scaners += quantity
        elif tech_type == x.title:
            Storage.stationery["xeroxes"] -= quantity
            Storage.xeroxes -= quantity
            destination.xeroxes += quantity
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
Storage.add_tech(p.title, 1)
Storage.add_tech(x.title, 5)
Storage.add_tech(s.title, 3)
Company.info()
Storage.info()
print()

bookkeeping = Company("Bookkeeping", 0, 0, 0)
human_resources_department = Company("HR Department", 0, 0, 0)
main_office = Company("Main Office", 0, 0, 0)

print(f"{36 * '* '}\nThe company decided to distribute some stationery from the storage\n{36 * '* '}")
Storage.tech_distribute("Printer", 1, bookkeeping)
Storage.tech_distribute("Scaner", 1, bookkeeping)
Storage.tech_distribute("Xerox", 1, bookkeeping)
Storage.tech_distribute("Xerox", 1, human_resources_department)
Storage.tech_distribute("Scaner", 1, human_resources_department)
Storage.tech_distribute("Xerox", 2, main_office)
Storage.tech_distribute("Scaner", 1, main_office)

Company.info()
Storage.info()
print()
bookkeeping.__str__()
human_resources_department.__str__()
main_office.__str__()

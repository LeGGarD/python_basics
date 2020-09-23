class Data:
    day = 0
    month = 0
    year = 0

    def __init__(self, data):
        self.data = data

    @classmethod
    def extract(cls, data):
        Data.day = int(data[0:1])
        Data.month = int(data[3:4])
        Data.year = int(data[6:9])

    @staticmethod
    def validate():
        if 1 <= Data.day < 32:
            print("Day checked")
        else:
            print("You printed wrong day")
        if 1 <= Data.month < 13:
            print("Month checked")
        else:
            print("You printed wrong month")
        if 1 <= Data.year < 9999:
            print("Year checked")
        else:
            print("You printed wrong year")
        if 1 <= Data.day < 32 and 1 <= Data.month < 13 and 1 <= Data.year < 9999:
            print("Validation succeed")
        else:
            print("Oops, something went wrong")


Data.extract("28-12-2019")
Data.validate()

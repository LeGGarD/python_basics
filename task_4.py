class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("The car is in motion!")

    def stop(self):
        print("The car has stopped")

    def turn(self, __direction):
        print(f"The car has turned to the {__direction}")

    def show_speed(self):
        print(f"The car is moving {self.speed}km/hour")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"The car is breaking the speed limit for {self.speed - 60}km/hour")
        else:
            print(f"The car is moving {self.speed}km/hour")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"The car is breaking the speed limit for {self.speed - 40}km/hour")
        else:
            print(f"The car is moving {self.speed}km/hour")


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


print(f"{36 * '- '}\nSome exmpls with police car\n{36 * '- '}")
police_car = PoliceCar(120, "Black", "Lamborghini", True)
police_car.go()
police_car.show_speed()
police_car.turn("right")

print(f"{36 * '- '}\nSome exmpls with town car\n{36 * '- '}")
town_car = TownCar(61, "White", "Toyota", False)
town_car.go()
town_car.show_speed()
print("The car is slowing down")
town_car.speed = 59
town_car.show_speed()
town_car.turn("left")

from time import sleep


class TrafficLight:
    __color = ""

    def running(self):
        n = 0
        while n < 3:
            __color = "red"
            print(__color)
            sleep(7)
            __color = "yellow"
            print(__color)
            sleep(2)
            __color = "green"
            print(__color)
            sleep(7)
            __color = "yellow"
            print(__color)
            sleep(2)
            n += 1


traff_light = TrafficLight()
traff_light.running()

class Car:
    name = ''
    engine = ''
    wheel_drive = ''
    hp = 0
    s = 0
    q = 0
    type = ''
    def __init__(self):
        print(f"CAR")
        self.name = "AUDI R8"
        self.engine = 'R8 Spyder V10 performance quattro'
        self.wheel_drive = 'trademark quattro permanent'
        self.hp = 750
        self.s = 900
        self.q = 1000
        self.type = 'sports sedan'
    def ShowOn(self):
        print(f"name: {self.name}, \nengine: {self.engine}, \nwheel drive: {self.wheel_drive},"
              f" \nHP: {self.hp}, \nHigh: {self.s}, \nweight: {self.q}, \ntype: {self.type}")
    def __del__(self):
        print("deleted objects of car")
if __name__ == '__main__':
    car = Car()
    car.ShowOn()
    del car
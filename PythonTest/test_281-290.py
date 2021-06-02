class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def info(self):
        print("바퀴수", self.wheel)
        print("가격", self.price)

#car = Car(2, 1000)
#print(car.wheel)
#print(car.price)

class Bicycle(Car):
    def __init__(self, wheel, price, drivetrain):
        super().__init__(wheel, price)  # = Car.__init__(wheel, price)
        #self.wheel = wheel
        #self.price = price
        self.drivetrain = drivetrain

    def info(self):
        super().info()
        print("구동계", self.drivetrain)

class Autocar(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)



#bicycle = Bicycle(2, 100, "시마노")
#print(bicycle.drivetrain)
#print(bicycle.price)

car = Autocar(4, 1000)
car.info()

bicycle = Bicycle(2, 100, "시마노")
bicycle.info()

class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")
    def 부모호출(self):
        super().호출()

나 = 자식()
나.호출()

class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    #self.손자 = 손자
    #print(self.손자)

나 = 자식()

class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()

나 = 자식()
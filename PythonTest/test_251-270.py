'''class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.gender))
    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __del__(self):
        print("나의 죽음을 알리지 말라")

areum = Human("모름", 0, "모름")
#print(areum.name)
#print(areum.age)
#print(areum.gender)
areum.who()
areum.setInfo("아름", 25, "여자")
del areum'''

class Stock:
    def __init__(self, name, code, per, pbr, rate):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.rate = rate
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def set_per(self, per):
        self.per = per
    def set_pbr(self, pbr):
        self.pbr = pbr
    def set_dividend(self, dividend):
        self.dividend = dividend

'''
samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(samsung.name)
print(samsung.code)
print(samsung.per)
print(samsung.pbr)
print(samsung.rate)
a = Stock(None, None)
a.set_name("삼성전자")
a.set_code("005930")
print(samsung.get_name())
print(samsung.get_code())
samsung.set_per(12.75)
'''
list = []
samsung_electronics = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
Hyundai_motor = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG_electronics = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

list.append(samsung_electronics)
list.append(Hyundai_motor)
list.append(LG_electronics)

for i in list:
    print(i.code, i.per)


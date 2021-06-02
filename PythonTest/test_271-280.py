import random

class Account():
    account_count = 0

    def __init__(self, name, balance):
        self.name = name  # 이름
        self.balance = balance  # 잔액
        self.bankname = "SC은행"  # 은행 이름
        num1 = str(random.randint(0, 999))  # 0부터 999까지의 숫자 중 하나를 랜덤으로 생성하고 int를 str로 변환
        num2 = str(random.randint(0, 99))  # 0부터 99까지의 숫자 중 하나를 랜덤으로 생성하고 int를 str로 변환
        num3 = str(random.randint(0, 999999))  # 0부터 999999까지의 숫자 중 하나를 랜덤으로 생성하고 int를 str로 변환

        num1 = num1.zfill(3)  # 문자열 앞에 빈칸을 0으로 채우기
        num2 = num2.zfill(2)  # 문자열 앞에 빈칸을 0으로 채우기
        num3 = num3.zfill(6)  # 문자열 앞에 빈칸을 0으로 채우기

        self.account_number = num1 + '-' + num2 + '-' + num3  # 계좌번호

        Account.account_count += 1
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

    def get_account_num(self):
        print(Account.account_count)

    def deposit(self, amount):
        if amount >=1:
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * 1.01

    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름:", self.bankname)
        print("예금주:", self.name)
        print("계좌번호:", self.account_number)
        print("잔고:", format(self.balance, ","))
    def withdraw_history(self):
        for amonut in self.withdraw_log:
            print(amonut)
    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)

cus_list = []

a = Account("파이썬", 20000)
b = Account("자바", 5000)
c = Account("R", 15000000)

'''cus_list.append(a)
cus_list.append(b)
cus_list.append(c)

for i in cus_list:
    if i.balance >= 1000000:
        i.display_info()'''



a.deposit(50000)
a.deposit(60000)
a.deposit_history()

a.withdraw(10000)
a.withdraw(20000)
a.withdraw(10000)
a.withdraw(10000)
a.withdraw_history()

'''Yun = Account("윤OO", 10000) # 이름과 초기 잔액 입력
david = Account("david", 100)
lily = Account("lily", 1000)
Yun.get_account_num()
Yun.deposit(10000)  # 예금
Yun.withdraw(5000)  # 출금
#print(Yun.bankname)
#print(Yun.name)
#print(Yun.account_number)
print(Yun.balance)
Yun.display_info()'''
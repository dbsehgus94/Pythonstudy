'''def print_coin():
    print("비트코인")
print_coin()

for i in range(100):
    print_coin()

def print_coins():
    for i in range(100):
        print("비트코인")

def 함수(문자열):
    print(문자열)
함수("안녕")
함수("Hi")

def print_with_smile(string):
    print(string+":D")

print_with_smile("안녕하세요")

def print_upper_price(price):
    print(price * 1.3)

def print_sum(a, b):
    print(a+b)

def print_arithmetic_operation(a, b):
    print(a,"+",b,"=",a+b)
    print(a,"-",b,"=",a-b)
    print(a,"*",b,"=",a*b)
    print(a,"/",b,"=",a/b)

print_arithmetic_operation(3, 4)

def print_max(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)

print_max(1, 100, 10000)

def print_reverse(string):
    print(string[::-1])

print_reverse("python")

def print_score(list):
    print(sum(list)/len(list))

print_score([1,2,3])

def print_even(list):
    for i in list:
        if i % 2 ==0:
            print(i)
print_even([1, 3, 2, 10, 12, 11, 15])

def print_keys(dic):
    for key, _ in dic.items():
        print(key)

    for i in dic.keys():
        print(i)

#print_keys({"이름":"김말똥", "나이":30, "성별":0})

import math
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(my_dict, key):
    print(my_dict[key])

print_value_by_key(my_dict, "10/26")


def print_5xn(string):
    print(string[0:5])
    print(string[5:])

print_5xn("아이엠어보이유알어걸")

def printmxn(string, num):
    Num = int(len(string)/num)
    for i in range(Num+1):
        print(string[i*num:i*num+num])
printmxn("아이엠어보이유알어걸", 3)

def calc_monthly_salary(annual_pay):
    monthly_pay = annual_pay / 12
    print(monthly_pay)
    print(round(monthly_pay, -1))
    print(math.floor(monthly_pay))
    print(math.ceil(monthly_pay))
    print(math.trunc(monthly_pay))

def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)
calc_monthly_salary(13700000)
'''
'''
def n_plus_1 (n) :
    result = n + 1
    return result
n_plus_1(3)
print(n_plus_1(3))
#print(result)

def make_url(string):
    #url = "www."+string+".com"
    #return url
    print(f"http://www.{string}.com")
print(make_url("naver"))
''''''
def make_list(string):
    list = []
    for i in string:
        list.append(i)
    return list

print(make_list("abcd"))

'''
def pickup_even(lists):
    list = []
    for i in lists:
        if i % 2 == 0:
            list.append(i)
    return list

print(pickup_even([3, 4, 5, 6, 7, 8]))

def convert_int(string) :
    return int(string.replace(',', ''))

print(convert_int(("1,234,567")))

def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
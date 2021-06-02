'''a = int(input("input number1: "))
b = int(input("input number2: "))
c = int(input("input number3: "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)'''

'''phone_number = input("휴대전화 번호 입력: ")
num = phone_number.split("-")[0]
num,_,_ = num.split("-")

if num == "011":
    a = "SKT"
elif num == "016":
    a = "KT"
elif num == "019":
    a = "LGU"
elif num == "010":
    a = "알수없음"
else:
    a = "???"
print(f"당신은 {a} 사용자입니다.")'''

'''a = input("우편번호: ")
a = a[0:3]
if a in ["010", "011", "012"]:
    print("강북구")
elif a in ["013", "014", "015"]:
    print("도봉구")
else:
    print("노원구")'''

'''a = input("주민등록번호: ")
a = a[7:8]
if a in ["1", "3"]:
    print("남자")
elif a in ["2", "4"]:
    print("여자")'''


'''a = input("주민등록번호: ")
b = a.split("-")[1][1:3]
if int(b[0]) == 0 and 0 <= int(b[1]) <= 8:
#if 0 <= int(b[0:2]) <= 8:
    print("서울 입니다.")
elif int(b[0]) == 0 and int(b[1]) == 9:
    print("부산 입니다.")
elif int(b[0]) == 1 and 0 <= int(b[1]) <= 2:
    print("부산 입니다.")
else:
    print("서울이 아닙니다.\n부산이 아닙니다.")'''

'''a = input('주민등록번호: ')
a = a.replace("-","")
cal1 = int(a[0])*2+int(a[1])*3+int(a[2])*4+int(a[3])*5+int(a[4])*6+int(a[5])*7+int(a[6])*8+int(a[7])*9+int(a[8])*2+int(a[9])*3+int(a[10])*4+int(a[11])*5
cal2 = 11 - (cal1 % 11)
cal3 = str(cal2)
#print(cal3)
if a[-1] == cal3:
    print("유효한 주민등록 번호")
else:
    print("유효하지 않은 주민등록 번호")'''

import requests
btc = requests.get("https://api.bithmub.com/public/ticker/").json()['data']
print(btc)

변동폭 = btc['max_price'] - btc['min_price']
최고가 = btc['max_price']
최저가 = btc['min_price']
시가 = btc['opening_price']

if (시가 + 변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")





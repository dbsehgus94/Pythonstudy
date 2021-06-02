#a =input("입력: ")
#print(a*2)

'''a = input("숫자를 입력하세요 : ")
if int(a) % 2 == 0:
    print("짝수")
else:
    print("홀수")'''
'''a = input("number : ")
num = int(a) + 20
if num > 255:
    print(255)
else:
    print(num)'''

'''a = input("현재시간:")
b = a.split(":")
if b[-1] == "00":
#if b[1] == "00":
#if a[-2] ==
#if a[3:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")'''

'''time = input("현재시간:")
a = time.replace(":", "")
min = int(a[0])*60 + int(a[1])
print(f"{a[0]}시 {a[1]}분 입니다.")
if min % 60 == 0:
if int(a) % 100 == 0:
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")'''


'''a = int(input("입력값: "))
b = a - 20
if b < 0:
    print("출력값: 0")
elif b > 255:
    print("출력값: 255")
else:
    print("출력값:", b)'''

'''fruit = ["사과", "포도", "홍시"]
a = str(input("좋아하는 과일은? "))
if a in fruit:
#if a == fruit[0] or a == fruit[1] or a == fruit[2]:
    print("냉장고에 있습니다.")
else:
    print("장보러 갈까요?")'''

'''warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
a = input("종목명을 입력하세요 : ")
if a in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")'''

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
a = input("제가좋아하는계절은:")
for k, v in fruit.items():
    if a == k: # key
        print("정답입니다")
        break
    elif a == v: # value
        print("정답입니다")
        break
    else:
        print("오답입니다")
        break

#if a in fruit:
#    print("정답입니다")
#else:
#    print("오답입니다")








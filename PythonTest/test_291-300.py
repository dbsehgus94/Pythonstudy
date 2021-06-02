'''f = open("C:/Users/Yun/Desktop/매수종목1.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420\n")
f.close()

f = open("C:/Users/Yun/Desktop/매수종목2.txt", mode="wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 네이버\n")
f.close()

import csv


with open("C:/Users/Yun/Desktop/매수종목.csv", mode="wt", encoding="cp949", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["종목명", "종목코드", "PER"])
    writer.writerow(["삼성전자", "005930", "15.79"])
    writer.writerow(["NAVER", "035420", "55.82"])'''
'''
f = open("C:/Users/Yun/Desktop/매수종목2.txt", encoding="utf-8")
lines = f.readlines()
#print(lines)
codes = {}
for line in lines:
    code = line.strip() # 특정 문자를 삭제
    #print(code)
    key, value = line.split()
    print(key, value)
    codes[key] = value

print(codes)
f.close()
'''
'''
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

'''
'''
per = ["10.31", "", "8.00"]
new_list = []
for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_list.append(v)
print(new_list)

'''
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        print("이상 없습니다.")
    finally:
        print("end")
'''       
try:
    실행코드
except:
    예외가 발생했을 때 수행할 코드
else:
    예외가 발생하지 않았을 때 수행할 코드
finally:
    예외 발생 여부와 상관없이 항상 수행할 코드
'''
'''
try:
    실행코드
except 예외 as 변수:
    예외처리코드'''
'''
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

'''
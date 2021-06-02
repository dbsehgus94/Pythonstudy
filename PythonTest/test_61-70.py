'''price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0:10:2])
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1:10:2])

nums = [1, 2, 3, 4, 5]
print(nums[::-1])
print(nums[-1:-6:-1])
nums.reverse()
print(nums)

interest = ['삼성전자', 'LG전자', 'Naver']
print("출력 예시:\n", interest[0], interest[2])

interest = ["삼성전자", "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]
#interest = interest(" ".join(interest))
print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest))
print(interest)

string = "삼성전자/LG전자/Naver"
a = string.split("/")
print(a)
# 문자열.split(구분자) -> 분리

data = [2, 4, 3, 1, 5, 10, 9]
data.sort(reverse=True)
data1 = sorted(data, reverse=True)
print(data1)'''

a = [1, 3, 5, 7]
a.insert(3,4)
print(a)
'''price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])

price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(i, price_list[i])
for i, data in enumerate(price_list):
    print(i, data)
for i in range(len(price_list)):
    print(i, price_list)

price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(3 - i, price_list[i])

price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)-1):
    print(100+10*i, price_list[i+1])'''

'''my_list = ["가", "나", "다", "라"]

for i in range(len(my_list)-1):
    print(my_list[i], my_list[i+1])

my_list = ["가", "나", "다", "라", "마"]

for i in range(len(my_list)-1):
    print(my_list[i], my_list[i+1], my_list[i+2])'''

'''my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
    print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 1 - i - 1])

my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(-(my_list[i]-my_list[i+1]))
    print(abs(my_list[i]-my_list[i+1]))
    print(my_list[i+1]-my_list[i])

my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-1):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)'''

low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(high_prices)):
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)






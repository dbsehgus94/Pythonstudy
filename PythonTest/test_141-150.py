'''리스트 = [100, 200, 300]
for i in 리스트:
    print(i+10)

리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print("오늘의 메뉴:", i)'''

'''리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))'''

'''리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i, len(i))

리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0])'''

'''리스트 = [1, 2, 3]
for i in 리스트:
    print("3 x", i)

리스트 = [1, 2, 3]
for i in 리스트:
    print("3 x", i,"=", 3*i)'''

'''리스트 = ["가", "나", "다", "라"]
#리스트 = 리스트[1:]
for i in 리스트[1:]:
    print(i)'''

'''리스트 = ["가", "나", "다", "라"]
for i in 리스트[0:3:2]:
#for i in 리스트[::2]:
    print(i)'''

리스트 = ["가", "나", "다", "라"]
리스트 = reversed(리스트)
for i in 리스트:
#for i in 리스트[::-1]:
    print(i)

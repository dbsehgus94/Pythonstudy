my_variable = ()
print(my_variable)
print(type(my_variable))

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

my_tuple = (1, ) # 하나의 데이터를 저장하는 경우 ,fmf 입력해야만 합니다.
print(type(my_tuple))

t = (1, 2, 3)
#t[0] = 'a'  튜플의 원소값은 수정이 불가능하다.
t1 = list(t)
print(t1)
t1[0] = 'a'
print(t1)
t = tuple(t1)
print(t)

t = ('a', 'b', 'c')
t1 = list(t)
t1[0] = 'A'
t = tuple(t1)
print(t)
t = ('A', 'b', 'c')
print(t)

interest = ('삼성전자', 'LKG 전자', 'SK Hynix')
interest1 = list(interest)
print(type(interest1))

interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest2 = tuple(interest)
print(type(interest2))

temp = ('apple', 'banana', 'cake')
a, b, c = temp # unpacking
print(a, b, c)
temp1 = 'apple', 'banana', 'tea', [0, 1], 1 # packing
print(temp1)

data = tuple(range(2, 100, 2))
print(data)
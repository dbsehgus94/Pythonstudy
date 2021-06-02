#for i in range(100):
#    print(i)
#for i in range(2002, 2051, 4):
#    print(i)
#for i in range(3, 31, 3):
#    print(i)
#for i in range(99, -1, -1):
#    print(i, end=' ')
#for i in range(100):
#    print(99 - i)
#for i in range(0, 10):
#    print("0."+str(i))
#for i in range(1, 10):
#    print("3X"+str(i),"=",str(3*i))
'''for i in range(1, 10, 2):
    print("3X"+str(i),"=",str(3*i))
    print(f"3X{i} = {3*i}")
a = 3
for i in range(1, 10):
    if i % 2 != 0:
        print('3X',a, "=", a*i)'''









total = 0
for i in range(1, 11):
    total = total + i
print(f"합 : {total}")

total = 0
for i in range(1, 11, 2):
    total += i
print(total)

total = 0
for i in range(0, 11, 2):
    total += i
print(total)

total = 1
for i in range(1, 11):
    total *= i
    print(total, i)


'''for i in range(10):
    print(i/10)
    print(i/10, i)
    print('0.'+str(i))
    print(i*0.1)
    print('%.2f' %(i*0.1))
for i in range(1, 10):
    print(f"3 x {i} = {3 * i}")'''

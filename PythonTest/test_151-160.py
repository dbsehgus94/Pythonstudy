'''리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i < 0:
        print(i)'''

'''list = [3, 100, 23, 44]
for i in list:
    if i % 3 == 0:
        print(i)'''

'''list = [13, 21, 12, 14, 30, 18]
for i in list:
    if i < 20:
        if i % 3 == 0:
            print(i)'''

'''list = ["I", "study", "python", "language", "!"]
for i in list:
    if len(i) >= 3:
        print(i)'''

'''list = ["A", "b", "c", "D"]
for i in list:
    if i.isupper() == True:
        print(i)

list = ["A", "b", "c", "D"]
for i in list:
    #if i.isupper() == False:
    #if i.isupper() != True:
    if i.islower():
        print(i)

list = ['dog', 'cat', 'parrot']
for i in list:
    print(i[0].upper()+i[1:])
    print(i.capitalize())
    print(i.title())
    print(i.replace(i[0], i[0].upper()))'''

'''list = ['hello.py', 'ex01.py', 'intro.hwp']
for i in list:
    a = i.split(".")
    print(a[0])'''

list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
    #if i[-1] == "h":
    #a = i.split(".")
    #if a[1] == "h":
    #    print(i)
    if i.find(".h") > 0:
        print(i)
    if i.count('.h') == True:
        print(i)

list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
    a = i.split(".")
    if a[1] == "h" or a[1] == "c":
        print(i)
    if i.split(".")[1] == "h" or i.split(".")[1] == "c":
        print(i)
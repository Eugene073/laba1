'''
Вариант 29.
Шеснадцатиричные числа, у которых 5 справа цифра равна В16, расположенные в порядке не убывания. Четные цифры выводить словами.
'''

def multiple_replace(numbers, dictionary):
    for i, j in dictionary.items():
        numbers = numbers.replace(i, j)
    return numbers

c = {'0' : 'ноль ', '1' : 'один ', '2' : 'два ', '3' : 'три ', '4' : 'четыре ',
     '5' : 'пять ', '6' : 'шесть ', '7' : 'семь ', '8' : 'восемь ', '9' : 'девять ',
     'A' : 'десять ', 'B' : 'одиннадцать ', 'C' : 'двенадцать ', 'D' : 'тринадцать ', 'E' : 'четырнадцать ', 'F' : 'пятнадцать '}


with open("test.txt", "r") as f:
    s = " "
    numbers = ""
    a = []
    while s != "":
        s = f.read(1)
        if (s != " ") and (s != "\n"):
            numbers =  numbers + s
        else:
            a.append(numbers)
            numbers = ""
a.append(numbers)

if len(a) == 1:
    print("Файл пуст")
    exit(0)

val = []
list = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F"]
for i in range(len(a)):
    a[i] = " ".join(a[i])
    a[i] = a[i].split()
    res = ""
    for j in range(len(a[i])):
        if a[i][j] in list:
            res = res + str(a[i][j])
        else:
            res = ""
            break
    if res != "":
        val.append(res)


main_val = []
for i in range(len(val)):
    if len(val[i]) > 4:
        if val[i][-5] == "B":
            if len(main_val)==0:
                main_val.append(val[i])
            else:
                if int(val[i], 16) >= int(main_val[-1], 16):
                    main_val.append(val[i])


if len(main_val)==0:
    print('В данной последовательности нет таких чисел')
    exit(0)


for i in range(len(main_val)-1):
    for j in range(len(main_val)-i-1):
        if int(main_val[j], 16) >= int(main_val[j+1], 16):
            x = main_val[j]
            main_val[j] = main_val[j+1]
            main_val[j+1] = x
        j += 1
    i += 1


for i in range(len(main_val)):
    if int(main_val[i], 16) % 2 == 0:
        main_val[i] = multiple_replace(main_val[i], c)
print(main_val)
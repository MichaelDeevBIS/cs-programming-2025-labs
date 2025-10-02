#(1 задание)
# x = 66
#y = 2.14
#z = 'Pop'
#w = True

#(2 задание)
# name = 'Миша'
#age = 18
#print(name, age)

#(3 задание)
# a = 342
#b = 56.2
#c = '43'
#d = a + b + int(c)
#print(d)

#(4 задание)
# a = 3
#b = 8
#c = (a + 4*b)*(a - 3*b) + a**2
#print(c)

#(5 задание)
#a = int(input("Введите длину"))
#b = int(input("Введите ширину"))
#d = (a + b)*2
#c = a*b
#print("Площадь прямоугольника равна" + str(c))
#print("Периметр прямоугольника равна" + str(d))

#(6 задание)
#print('*   *   * ' )
#print(' * * * *' )
#print('  *   *' )


#(7 задание)
#a = 6
#b = 10
#op1 = a + b
#op2 = a - b
#op3 = a*b
#op4 = a/b
#op5 = a//b
#op6 = a%b
#op7 = a**b
#sr1 = a == b
#sr2 = a != b
#sr3 = a > b
#sr4 = a < b
#sr5 = a >= b
#sr6 = a <= b
#print(op1, op2, op3, op4, op5, op6, op7, sr1, sr2, sr3, sr4, sr5, sr6 )


#(8 задание)
#name = 'Миша'
#age = '18'
#print(f'Меня зовут {name} , мне {age} лет')

#(9 задание)
#a = 'Cъешь ещё '
#b = 'этих мягких '
#c = 'французких булок, '
#d = 'да выпей '
#e = 'чаю '
#print(a + b + c + d + e)


#(10 задание)
#print('Нет! Да! ' *4)


#(12 задание)
#a = str(input("Введите слово, содержащие не менее 10 символов: "))
#print(str(a[0:4]))
#print(str(a[-2:]))
#print(str(a[4:8]))
#print(str(a[::-1]))


#(11 задание)
n = input("Введите три числа, разделенных запятой")
numbers = n.split(',')
num1 = int(numbers[0])
num2 = int(numbers[1])
num3 = int(numbers[2])
r = (num1 + num3) // num2
print('Результата вычисления: ' + str(r))


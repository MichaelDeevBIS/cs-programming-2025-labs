#1задание
name1 = input('Введите ваше имя: ')
age1 = input('Введите ваш возраст:')
for i in range (10):
    print(f'Меня зовут {name1} и мне {age1} лет')

#2задание
num2 = input('Введите число от 1 до 9: ')
k=1
for i in range (10):
    print(f'{num2} * {k} = {int(num2) *k}')
    k=k+1

#3задание
for i in range (0, 101, 3):
    print(i)

#4задание
num4 = input('Введите число: ')
k=1
for i in range (1, int(num4)+1):
    k=k*i
print(k)

#5задание
k = 20
while k>=0:
    print(k)
    k=k-1

#6задание
num6 = input('Введите число: ')
a, b = 0, 1
while a <= int(num6):
    print(a, end=" ")
    a, b = b, a + b

#7задание
word = input('Введите слово: ')
k=0
for i in range (len(word)):
    print(str(word[k])+str((k+1)), end='')
    k=k+1

#8задание
k=0
while k == 0:
    n = input('Введите два числа через пробел: ')
    nums = n.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    r = num1 + num2
    print(f'Сумма равна: {r}')

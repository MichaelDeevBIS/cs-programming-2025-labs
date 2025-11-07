#1задание
temp = int(input('Введите температуру: '))
if temp >= 20:
    print('Кондиционер выключен')
else:
    print('Кондиционер включен')


#2задние
month = int(input('Введите номер месяца: '))
if month == 12 or month <=2:
    print('Это зима')
if 2 < month < 6:
    print('Это весна')
if 5 < month < 9:
    print('Это лето')
if 8 < month < 12:
    print('Это осень')


#3задание
try:
    age = int(input('Введите возраст собаки (в годах): '))
    k = 0
    if 0 < age < 3:
        k = k + 10.5*age
    elif 2 < age < 23:
        k = 21 + 4*(age-2)
        print(f'Возраст собаки в человеческих годах: {k}')
    if age < 1:
        print('Ошибка: возраст должен быть не меньше 1')
    elif age > 22:
        print('Ошибка: возраст должен быть не больше 22')
except ValueError:
    print('Ошибка: введено не число')


#4задание
s = input('Введите число: ')
if int(s[-1])%2==0 and (s.count('1')+s.count('2')*2+s.count('3')*3+s.count('4')*4+s.count('5')*5+s.count('6')*6+s.count('7')*7+s.count('8')*8+s.count('9')*9)%3==0:
    print('Ваше число делится на 6')
else:
    print('Ваше число не делится на 6')


#5задание
p = input("Придумайте пароль: ")
if len(p) < 8:
    print("Пароль ненадежный: лишком короткий пароль (меньше восьми символов)")
if p.upper() == p:
    print("Пароль ненадежный: нет заглавных букв")
if p.lower() == p:
    print("Пароль ненадежный: нет строчных букв")
if not any(char in "0123456789" for char in p):
    print("Пароль ненадежный: нет цифр")
if p.isalnum():
    print("Пароль ненадежный: нет специальных символов")
if (len(p) >= 8 and p.upper() != p and p.lower() != p and any(char in "0123456789" for char in p) and not p.isalnum()):
    print("Пароль надежный")


#6задание
year = int(input('Введите год: '))
if year % 4 == 0:
   if year % 100 != 0 or year % 400 == 0:
      print('Високосный год')
   else:
      print('Не високосный год')
else:
   print('Не високосный год')


#7задание
n = input('Введите три числа: ')
num = n.split()
num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])
if num1 < num2 and num1 < num3:
   print(f'Наименьшее число: {num1}')
elif num2 < num1 and num2 < num3:
   print(f'Наименьшее число: {num2}')
else:
   print(f'Наименьшее число: {num3}')


#8задание
s = int(input('Введите сумму покупки: '))
if s < 1000:
   k = 0
   print('Ваша скидка равна: 0%')
elif 1000 <= s < 5001:
   k = 5
   print('Ваша скидка равна: 5%')
elif 5000 <= s <= 10000:
   k = 10
   print('Ваша скидка равна: 10%')
elif s > 10000:
   k = 15
   print('Ваша скидка равна: 15%')
s1 = s * ((100 - k)/100)
print(f'К оплате: {s1}')


#9задание
hour = int(input('Введите час (0-23): '))
if 0 <= hour < 6:
   print('Сейчас ночь')
elif 6 <= hour < 12:
   print('Сейчас утро')
elif 12 <= hour < 18:
   print('Сейчас день')
elif 18 <= hour < 24:
   print('Сейчас вечер')


#10задание
try:
    num = int(input('Введите число: '))
    if num > 1:
        for i in range (2, num):
            if num % i == 0:
                print(f'{num} - составное число')
                break
        else:
            print(f'{num} - простое число')
    else:
        print('Ошибка: введено число меньше одного')
except ValueError:
    print('Ошибка: введено не число')


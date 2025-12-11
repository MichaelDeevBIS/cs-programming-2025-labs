#1задание
num = int(input('Введите число: '))
time = input('Введите исходную еденицу измерения:  ')
next_time = input('Введите еденицу измерения, в которую нужно перевести:  ')
def calc(num, time, next_time):
    if time == 'h' and next_time == 's':
        r = num * 3600
    if time == 'h' and next_time == 'm':
        r = num * 60
    if time == 'm' and next_time == 'h':
        r = round(num / 60, 4)
    if time == 'm' and next_time == 's':
        r = num * 60
    if time == 's' and next_time == 'h':
        r = round(num / 3600, 4)
    if time == 's' and next_time == 'm':
        r = round(num / 60, 4)
    print(f'Ваш результат: {r}{next_time}')
calc(num, time, next_time)


#2задание
def calculate_profit():
    a = int(input('Введите сумму вклада: '))
    years = int(input('Введите количество лет: '))
    if a < 30000:
        print('Минимальный вклад 30000 рублей!')
        return
    k = a // 10000
    if k > 5:
        k = 5
    else:
        k = k
    vklad = a
    for year in range(1, years + 1):
        if year <= 3:
            stav = 3
        elif 4 <= year <= 6:
            stav = 5
        else:
            stav = 2
        r = (stav + k) / 100
        vklad = vklad * (1 + r)
    prib = round(vklad - a, 2)
    print(f'Сумма прибыли равна: {prib}')
calculate_profit()


#3задание
def easy_number():
    start = int(input('От какого числа: '))
    end = int(input('До какого числа: '))
    if start > end:
        print('Error!')
    else:
        my_list = []
        for i in range(start, end + 1):
            if i > 1:
                for n in range(2, i):
                    if i % n == 0:
                        break
                else:
                    my_list.append(i)
        if not my_list:
            print('Error!')
        else:
            print(f'Простые числа в диапозоне от {start} до {end}: {my_list}')
easy_number()


#4задание
def matrica():
    n = int(input())
    if n >2:
        mat1 = [list(map(int, input().split())) for x in range(n)]
        mat2 = [list(map(int, input().split())) for y in range(n)]
        if any(len(res) != n for res in mat1 + mat2):
            print('Error!')
        else:
            for i in range(n):
                res = [mat1[i][j] + mat2[i][j] for j in range(n)]
                print(' '.join(map(str, res)))
    else:
        print('Error!')
matrica()


#5задание
def palindrom():
    n = input('Введите строку: ')
    r = n.replace(' ', '')
    r1 = r.lower()
    if r1 == r1[::-1]:
        print('Да')
    else:
        print('Нет')
palindrom()
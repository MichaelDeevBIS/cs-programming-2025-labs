#1задание
num = int(input('Введите число: '))
time = input('Введите исходную еденицу измерения:  ')
next_time = input('Введите еденицу измерения, в которую нужно перевести:  ')
def calc(num, time, next_time):
    if time == 'h' and next_time == 's':
        r = num * 3600
    elif time == 'h' and next_time == 'm':
        r = num * 60
    elif time == 'm' and next_time == 'h':
        r = round(num / 60, 4)
    elif time == 'm' and next_time == 's':
        r = num * 60
    elif time == 's' and next_time == 'h':
        r = round(num / 3600, 4)
    elif time == 's' and next_time == 'm':
        r = round(num / 60, 4)
    print(f'Ваш результат: {r}{next_time}')
calc(num, time, next_time)


#2задание
a = int(input('Введите сумму вклада: '))
years = int(input('Введите количество лет: '))
def calculate_profit(a, years):
    if a < 30000:
        print('Минимальный вклад 30000 рублей!')
        return
    k = (a // 10000) * 0.3
    if k > 5:
        k = 5
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
calculate_profit(a, years)


#3задание
start = int(input('От какого числа: '))
end = int(input('До какого числа: '))
def easy_number(start, end):
    if start > end:
        print('Error!')
        return
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
            return
        else:
            print(f'Простые числа в диапозоне от {start} до {end}: {my_list}')
easy_number(start, end)


#4задание
n = int(input())
def matrica(n):
    if n >2:
        mat1 = [list(map(int, input().split())) for x in range(n)]
        mat2 = [list(map(int, input().split())) for y in range(n)]
        if any(len(res) != n for res in mat1 + mat2):
            print('Error!')
            return
        else:
            for i in range(n):
                res = [mat1[i][j] + mat2[i][j] for j in range(n)]
                print(' '.join(map(str, res)))
    else:
        print('Error!')
        return
matrica(n)


#5задание
n = input('Введите строку: ')
def palindrom(n):
    r = n.replace(' ', '')
    r1 = r.lower()
    if r1 == r1[::-1]:
        print('Да')
    else:
        print('Нет')
palindrom(n)

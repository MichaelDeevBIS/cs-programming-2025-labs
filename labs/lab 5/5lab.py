#задание 1
# numbers = [2, 1, 5, 8, 5, 3, 4, 7, 6, 10, 9]
# k = 0
# for i in numbers:
#     if numbers[k]-3 != 0:
#         k = k +1
#     else:
#         numbers[k] = 30
# print(numbers)


#задание 2
# numbers = [2, 3, 4, 5, 6]
# numbers1 = [x**2 for x in numbers]
# print(numbers1)


#задание 3
# numbers = [3, 4343, 765, 33, 30933, 5]
# print(max(numbers)/len(numbers))


#задание 4
data = (3, 1, 2, 'apple', 55, 'green')
try:
    r = tuple(sorted(data))
except TypeError:
    r = data
print(r)
   



#задание 5
# products = {'молоко': 100, 'хлеб': 25, 'яблоко': 75, 'сок': 80, 'конфеты': 150}
# pr1 = min(products, key=products.get)
# pr2 = max(products, key=products.get)
# print(f'товар с минимальной ценой: {pr1}')
# print(f'товар с максимальной ценой: {pr2}')


#задание 6
# my_list = [1, 2, 55, 'список', 'банан']
# my_dict = {item: item for item in my_list}
# print(my_dict)


#задание 7
# en_ru_dict = {'apple': 'яблоко','sock': 'носок','mouse': 'мышь','brain': 'мозг','cool': 'круто'}
# ru_en_dict = {value: key for key, value in en_ru_dict.items()}
# word = input('Введите слово на русском: ')
# if word in ru_en_dict:
#     print(f'Перевод слова: {ru_en_dict[word]}')

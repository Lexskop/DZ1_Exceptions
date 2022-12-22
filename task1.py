# Реализуйте 3 метода, чтобы в каждом из них получить разные исключения

def meth_first():
    a = int(input('Введите целое число А -> '))
    b = int(input('Введите целое число B. Для получения исключения введите 0 -> '))
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Делить на ноль нельзя! ZeroDivisionError')

def meth_second():
    c = [1, 2, 3]
    index = int(input('Введите индекс. Для получения исключения введите значение индекса больше 2 -> '))
    try:
        print(c[index])
    except IndexError:
        print('Значения с таким индексом в массиве нет! IndexError')

def meth_third():
    spices = dict()
    spices = {'s1': 'соль', 'f': 'перец','s2': 'сахар'}
    word = input('Введите любое значение из словаря: s1 f s2. Для получения исключения введите любое другое слово -> ')
    try:
        print(spices[word])
    except KeyError:
        print('Такого слова в словаре нет! KeyError')

while True:
    choice_meth = input('Введите номер метода (1,2,3) -> ')
    if choice_meth == '1':
        meth_first()
    elif choice_meth == '2':
        meth_second()
    elif choice_meth == '3':
        meth_third()
    else:
        print('Bye!')
        break
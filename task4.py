# * Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив, каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке. 
# Если длины массивов не равны, необходимо как-то оповестить пользователя. 
# Важно: При выполнении метода единственное исключение, которое пользователь может увидеть - RuntimeException, т.е. ваше.

import random

def difference_of_n():
    a = [random.randint(0,5) for x in range(random.randint(1,2))]
    b = [random.randint(0,5) for x in range(random.randint(1,2))]
    c = []
    print(f'Получили два случайных массива -> ',a,b)
    try:
        if len(a)==len(b):
            for i in range(len(a)):
                c.append(a[i] / b[i])
            return c
        else:
            return 'Один массив больше другого!'
    except ZeroDivisionError:
        return 'Делить на ноль нельзя. RuntimeException'

print(difference_of_n())
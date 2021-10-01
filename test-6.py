programm = True
while programm:
    a = []
    flag = True
    print('Сколько элементов вы желаете хранить в массиве array? \nВведите целочисленное положительное значение: ')
    while flag:
        try:
            num = int(input())
        except ValueError:
            print('Ошибка, количество элементов массива должно быть положительным, целым и больше единицы. \nПовторите ввод: ')
        else:
            if num < 0:
                print('Вы ввели отрицательное значение или текст, ошибка. \nПовторите ввод: ')
            if num == 0:
                print('В массиве не может содержаться ноль элементов. \nПовторите ввод: ')
            if num == 1:
                print('Выполнение поставленной задачи с одним элементом массива невозможно. \nЕсли в массиве будет содержаться один элемент, то станет невозможным нахождение второго элемента отличающигося на delta. \nПовторите ввод: ')
            if num > 1:
                flag = False
    print('Введите значения для', num, 'элементов массива.')
    for i in range(0, num):
        print('Введите значение для', i + 1, 'элемента')
        flag = True
        while flag:
            try:
                q = int(input())
            except ValueError:
                print('Ошика. Вы ввели не целое вещетвенное число или текст. \nПовторите ввод:')
            else:
                flag = False
        a.append(q)
    print('Введите значение переменной DELTA: ')
    flag = True
    while flag:
        try:
            q = int(input())
        except ValueError:
            print('Ошика. проведение операции с использованием введённой переменной DELTA невозможна. \nЗначение DELTA должно быть целым и неотрицательным. \nПовторите ввод: ')
        else:
            if q < 0:
                print('вы ввели отрицательное значение. \nПовторите ввод:')
            else:
                flag = False
    delta = q
    print('Ответ: ', a.count(min(a) + delta))
    print('Все операции были проведены, необходимо повторное использование программы с другими числами? Ответьте yes/no.')
    flag = True
    while flag:
        answer = input().lower()
        if answer == 'yes' or answer == 'no':
            flag = False
        else:
            print('Введите ответ в виде yes или no')
    if answer == 'no':
        programm = False
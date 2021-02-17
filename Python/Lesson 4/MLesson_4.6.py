# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

def gen_num():
    print('To star the program "Generation of numbers" press "ENTER"\n')

    for i in count(int(input('Enter the number: '))):
        print(f'Next number {i}\n')
        stop = input('For continue press "ENTER"\nFor exit press "Q"\n---> ... ')
        if stop == 'Q' or stop == 'q':
            print('\nThe program was stopped.\n')
            break

def gen_list():
    print('To star the program "Generation of list" press "ENTER"\n')
    stop = input('For continue press "ENTER"\nFor exit press "Q"\n---> ... ')
    if stop == 'Q' or stop == 'q':
        return print('\nThe program was stopped.\n')
    else:
        new_list = input('Enter the elements of the new list separated by a space: ').split()
        i = 0
        for el in cycle(new_list):
            if i <= 10:
                print(el)
                i += 1
            else:
                break

gen_num()
gen_list()

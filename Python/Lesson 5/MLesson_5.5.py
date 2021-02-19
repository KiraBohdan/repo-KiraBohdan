# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('Numbers_list.txt', 'w', encoding='utf-8') as f:
    f.write(f'{" ".join([str(i) for i in range(1, 101)])}')

with open('Numbers_list.txt', 'r', encoding='utf-8') as f:
    numbers = [int(i) for i in f.read().split()]
    print(f'Сумма всех числел в файле: {sum(numbers)}')

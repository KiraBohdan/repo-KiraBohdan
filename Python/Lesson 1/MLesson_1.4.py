# task_4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное чичло: '))

max_number = number % 10
new_number = number // 10

while new_number != 0:
    i = new_number % 10
    if i > max_number:
        max_number = i
    else:
        new_number = new_number // 10

print('Самая большая цифра из числа:', max_number)
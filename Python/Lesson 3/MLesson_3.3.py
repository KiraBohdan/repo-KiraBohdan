# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    if (num_1 < num_2) and (num_1 < num_3):
        return f'Сумма максимальных значений: {num_2 + num_3}'
    elif (num_1 > num_2) and (num_1 < num_3):
        return f'Сумма максимальных значений: {num_1 + num_3}'
    else:
        return f'Сумма максимальных значений: {num_1 + num_2}'

print(my_func(0, 8, 1))

# task_3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

n = input('Введите число n: ')
nn = n + n
nnn = n + n + n

print('Сумма чисел в формете "n + nn + nnn":', int(n) + int(nn) + int(nnn))
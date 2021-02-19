# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

new_data = []
lines = int(input('Сколько строк вы хотите ввести: '))

for i in range(lines):
    new_data.append(input('Введите данные для записи в файл: '))
    new_data.append('\n')

with open('Data.txt', 'w') as f:
    f.writelines(new_data)

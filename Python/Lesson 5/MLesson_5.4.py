# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

num_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('Numbers_en.txt', 'r', encoding='utf-8') as f_1:
    with open('Numbers_ru.txt', 'w', encoding='utf-8') as f_2:
        for line in f_1:
            en, *num = line.split()
            ru = num_dict[en]
            f_2.write(' '.join([ru] + num) + '\n')

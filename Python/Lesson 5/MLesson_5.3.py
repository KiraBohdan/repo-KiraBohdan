# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# ------>
# Personal.txt:
# Max - 18000
# Leo - 19000
# Kate - 21000

with open('Personal.txt', 'r') as f:
    person = f.readlines()
    name = []
    salary = []
    for i in person:
        i.replace('\n', '')
        pers_list = i.split()
        name.append(pers_list[0])
        salary.append(int(pers_list[2]))

    x = 0
    for j in salary:
        if j < 20000:
            print(f'Зарплата ниже 20 тыс. ---> {name[x]}')
            x += 1

    print(f'Средний заработок сотрудников: {int(sum(salary) / len(salary))}')

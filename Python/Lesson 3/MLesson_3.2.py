# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def person(first_name, second_name, date, city, email, phone):
    return f'Name: {first_name} {second_name} | Date: {date} | City: {city} | @mail: {email} | Phone: {phone}'

print(person(first_name='Kira', second_name='Bohdan', date='09.09.1989', city='Minsk', email='kira.bohdan@gmail.com', phone='+375336648448'))

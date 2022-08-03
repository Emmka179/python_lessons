# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
if 1 <= month <= 12:
    print('Вы ввели', month, 'месяц')
else:
    print('Вы ввели неверный месяц')

if month == 1:
    print(31)
if month == 2:
    print(28)
if month == 3:
    print(31)
if month == 4:
    print(30)
if month == 5:
    print(31)
if month == 6:
    print(30)
if month == 7:
    print(31)
if month == 8:
    print(31)
if month == 9:
    print(30)
if month == 10:
    print(31)
if month == 11:
    print(30)
if month == 12:
    print(31)

#TODO здесь ваш код

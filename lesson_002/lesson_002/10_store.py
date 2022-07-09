#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
print("На складе лежит ламп на сумму - ", lamps_cost)
print('------------------------------')
# или проще (/сложнее ?)

tables_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
tables_cost_2 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
print("На складе лежит одних столов на сумму - ", tables_cost)
print("На складе лежит других столов на сумму - ", tables_cost_2)
print('------------------------------')

sofas_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sofas_cost_2 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
print("На складе лежит одних диванов на сумму - ", sofas_cost)
print("На складе лежит других диванов на сумму - ", sofas_cost_2)
print('------------------------------')

chairs_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
chairs_cost_2 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
chairs_cost_3 = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
print("На складе лежит одних стульев на сумму - ", chairs_cost)
print("На складе лежит вторых стульев на сумму - ", chairs_cost_2)
print("На складе лежит третьих стульев на сумму - ", chairs_cost_3)
print('------------------------------')

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
print('------------------------------')

table_code = goods['Стол']
tables_item = store[table_code][0]
tables_quantity = tables_item['quantity']
tables_price = tables_item['price']
tables_cost = tables_quantity * tables_price
print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')
print('------------------------------')

table_code_2 = goods['Стол']
tables_item_2 = store[table_code_2][1]
tables_quantity_2 = tables_item_2['quantity']
tables_price_2 = tables_item_2['price']
tables_cost_2 = tables_quantity_2 * tables_price_2
print('Стол(2) -', tables_quantity_2, 'шт, стоимость', tables_cost_2, 'руб')
print('------------------------------')

sofa_code = goods['Диван']
sofas_item = store[sofa_code][0]
sofas_quantity = sofas_item['quantity']
sofas_price = sofas_item['price']
sofas_cost = sofas_quantity * sofas_price
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')
print('------------------------------')

sofa_code_2 = goods['Диван']
sofas_item_2 = store[sofa_code_2][1]
sofas_quantity_2 = sofas_item_2['quantity']
sofas_price_2 = sofas_item_2['price']
sofas_cost_2 = sofas_quantity_2 * sofas_price_2
print('Диван(2) -', sofas_quantity_2, 'шт, стоимость', sofas_cost_2, 'руб')
print('------------------------------')

chair_code = goods['Стул']
chairs_item = store[chair_code][0]
chairs_quantity = chairs_item['quantity']
chairs_price = chairs_item['price']
chairs_cost = chairs_quantity * chairs_price
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')
print('------------------------------')

chair_code_2 = goods['Стул']
chairs_item_2 = store[chair_code_2][1]
chairs_quantity_2 = chairs_item_2['quantity']
chairs_price_2 = chairs_item_2['price']
chairs_cost_2 = chairs_quantity_2 * chairs_price_2
print('Стул(2) -', chairs_quantity_2, 'шт, стоимость', chairs_cost_2, 'руб')
print('------------------------------')

chair_code_3 = goods['Стул']
chairs_item_3 = store[chair_code_3][2]
chairs_quantity_3 = chairs_item_3['quantity']
chairs_price_3 = chairs_item_3['price']
chairs_cost_3 = chairs_quantity_3 * chairs_price_3
print('Стул(3) -', chairs_quantity_3, 'шт, стоимость', chairs_cost_3, 'руб')
print('------------------------------')


# TODO: добавь итоговый вывод сколько всего ламп, сколько всего стульев...
#  Формат вывода:
# 	Лампа - 27 шт, стоимость 1134
# 	Стол - xxx шт, стоимость xxx
# 	Диван - xxx шт, стоимость xxx
# 	Стул - xxx шт, стоимость xxx

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################

#11 task completed

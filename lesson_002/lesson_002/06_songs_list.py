#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
#
# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# halo = songs_1['Halo', 4.9]
# enjoy = songs_1['Enjoy the Silence', 4.20]
# clean = songs_1['Clean', 5.83]

songs_1 = violator_songs_list
songs_sum = songs_1[3] + songs_1[5] + songs_1[8]
sum = songs_sum[1] + songs_sum[3] + songs_sum[5]
print("Три песни звучат ", round(sum, 2), "минут")

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

songs_2 = violator_songs_dict
# TODO: можешь сразу назвать переменную total. Или используй внутри print'а переменную songs_sum_2
total = songs_2['Sweetest Perfection'] + songs_2['Policy of Truth'] + songs_2['Blue Dress']
# TODO: верни округление: внутри {.....} можно не только переменные подставлять, то вызывать функции и другие операции.
#  Пример:
#       print(f'{2 + 2 * 100} = 202')
print(f'А другие три песни звучат {round(total, 2)} минут')


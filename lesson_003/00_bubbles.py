# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(600, 300)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius, width=2)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
#     Функции и методы должны носить названия-действия. А объекты - названия-существительные. И bubble сейчас как раз
def bubble_draw(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        color = sd.random_color()
        sd.circle(center_position=point, color=color, radius=radius, width=2)

point = sd.get_point(600, 300)
#bubble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд             # TODO: пусть будут зелеными
# for x in range(150, 1101, 100):
#     point = sd.get_point(x, 300)
#     bubble_draw(point=point, step=10)

# Нарисовать три ряда по 10 пузырьков       # TODO: пусть будут красными
# def bubble(point, step):
#     radius = 50
#     for _ in range(1):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# for y in range(200, 401, 100):        # TODO: нейминг правильный, читается легко и понятно 👍👍
#     for x in range(150, 1101, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=10)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# def bubble(point, step):
#     radius = 50
#     for _ in range(1):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    # TODO: почему цвет не стал красным?
    color = sd.COLOR_RED
    bubble_draw(point=point, step=step)

sd.pause()

# TODO: в названии слова местами только поменяй: draw_bubble, т.к. глагол пишут первее

# TODO: остается разобраться с цветом.

# TODO: раскоментируй весь код в файле (ничего страшного, что все в кучу выводит), щас в коде 2 почти одинаковые функции
#  объявлены, а я говорил оставить одну. Так же надо везде заменить вызов со старого названия bubble\bubble_draw на
#  draw_bubble. Свой код не превращай в комменты, пока отлаживаешь - можно, но на проверку присылай незакомментированным
#  чтобы я понимал, где старье, а где свежак + PyCharm не ругается на закомментированный код, не проверяет синтаксис

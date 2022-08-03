# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(600, 300)
# sd.circle(center_position=point)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius, width=2)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# def bubble(point, step):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
#
# point = sd.get_point(600, 300)
# bubble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд
# def bubble(point, step):
#     radius = 50
#     for _ in range(1):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# for x in range(150, 1101, 100):
#     point = sd.get_point(x, 300)
#     bubble(point=point, step=10)

# Нарисовать три ряда по 10 пузырьков
# def bubble(point, step):
#     radius = 50
#     for _ in range(1):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# for y in range(200, 401, 100):
#     for x in range(150, 1101, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=10)



# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# def bubble(point, step):
#     radius = 50
#     for _ in range(1):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# for _ in range(100):
#     point = sd.random_point()
#     step = random.randint(2, 10)
#     bubble(point=point, step=step)

sd.pause()



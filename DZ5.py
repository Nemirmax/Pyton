# Задача 5. Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.

print()

print('Семинар 1')

xA = int(input('Введите координату Xa = '))

yA = int(input('Введите координату Ya = '))

xB = int(input('Введите координату Xb = '))

yB = int(input('Введите координату Yb = '))

dist = ((xB - xA)**2 + (yB - yA)**2)**0.5

print(f'Расстояние между точками равно {round(dist, 2)}')

print('Конец')

print()
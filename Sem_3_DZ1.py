# Задача 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных 
# позициях элементы 3 и 9, ответ: 12

print()
print('Семинар 3')
import random
n = int(input ('Введите количество чисел в списке n: '))
coll =[]
for i in range(0, n):
    t = random.randint(0, 99)
    coll.append(t)
print(coll)

print('На нечетных позиция стоят следующие элементы:', end = ' ')
sum = 0
for i in range (0, n):
    if i % 2 != 0:
        sum += coll[i]
        print (coll[i], end = ' ')
print()
print(f'Сумма элементов на нечетных позициях равна: {sum}')
print('Конец')
print()
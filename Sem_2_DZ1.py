# Задача 1. Напишите программу, которая принимает на вход
# число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ]
# (1, 1*2, 1*2*3, 1*2*3*4)

print()
print('Семинар 2')
multiplication = 1
coll = []
n = int(input('Введите количество чисел n: '))
for i in range(1, n + 1):
    multiplication *= i
    coll.append(multiplication)
print(f'n = {n} -> {coll}')
print('Конец')
print()
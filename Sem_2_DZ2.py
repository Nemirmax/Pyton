# Задача 2. Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print()
print('Семинар 2')
n = int(input('Введите количество чисел n: '))
coll = []
sum = 0
for i in range(1, n + 1):
    temp = (1 + 1/i)**i
    sum += temp
    t = str(i) + ': ' + str(round(temp, 3))
    coll.append(t)
print('n =', n, ':', coll)
print(f'Сумма чисел последовательности равна {round(sum, 3)}')
print('Конец')
print()
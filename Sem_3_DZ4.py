#Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

print()
print('Семинар 3')
n = int(input('Введите десятичное число N = '))
temp = n
number = ''
while n > 0:
    number = str(n%2) + number
    n//=2
print(f'Число {temp} в двоичной системе равно: {number}')
print('Конец')
print()
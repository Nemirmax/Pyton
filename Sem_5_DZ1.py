# Напишите программу, удаляющую из текста все слова, содержащие "абв".

print()

print('Семинар 5')

text = input('Введите текст: ')
text = list(filter(lambda x: 'абв' not in x, text.split()))
print(" ".join(text))

print('Конец')

print()
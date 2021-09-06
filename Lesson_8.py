# Посчитать, сколько раз встречается определенная цифра в введенной
# последовательности чисел. Количество вводимых чисел и цифра, которую необходимо
# посчитать, задаются вводом с клавиатуры.
n = int(input('Введите, сколько чисел вы будете вводить: '))
digit = input('Какую цифру будем подсчитывать в последовательности чисел? ')
summ = 0
for i in range(n):
    j = input(f'Введите число {i + 1}: ')
    summ += j.count(digit)
print(f'Цифра {digit} встечается в последовательности {summ} раз')
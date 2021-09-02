# Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если
# надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на
# экран любой символ алфавита от 'a' до 'f' включительно.

import random

print('Случайное целое число:')
number_start_range = int(input('Начало границы: '))
number_end_range = int(input('Конец границы: '))

print('Случайное вещественное число:')
float_start_range = float(input('Начало границы: '))
float_end_range = float(input('Конец границы: '))

print('Случайны символ:')
symbol_start_range = ord(input('Начало границы (символ): '))
symbol_end_range = ord(input('Конец границы (символ): '))

number_random = random.randint(number_start_range, number_end_range)
float_random = random.uniform(float_start_range, float_end_range)
symbol_random = chr(random.randint(symbol_start_range, symbol_end_range))

print(f'Случайное целове число: {number_random}')
print(f'Случайное вещественное число: {float_random}')
print(f'Случайный символ: {symbol_random}')

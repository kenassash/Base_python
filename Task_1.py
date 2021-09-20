# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Выделяемая память - 80 байт
# ОС(Windows) 64bit, Python 3.8.6 64bit

from sys import getsizeof


def recursion(n, a):
    if n == 1:
        return a
    else:
        return a + recursion(n - 1, a * (-0.5))


def func_sum_bytes(variables):
    sum_bytes = 0
    for i in variables:
        sum_bytes += getsizeof(i)
    return sum_bytes


n = 10
a = 1

result = recursion(n, a)

variables = [n, a, result]

b = func_sum_bytes(variables)
print(f'Количество выделяемой памяти - {b} байт')
print(result)

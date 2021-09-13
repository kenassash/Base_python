#  Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
#  Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile


# Первый вариант решения (Решето Эратосфена)
def sieve(n):
    element = [i for i in range(n)]
    element[1] = 0
    for i in range(2, n):
        if element[i] != 0:
            j = i * 2
            while j < n:
                element[j] = 0
                j += i
    result = [i for i in element if i != 0]
    return result


# Конец первого варианта решения

cProfile.run('sieve(1000000)')


# 0.591 seconds

# Вывод простых чисел вплоть до n
def prime(n):
    n = int(n)
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


cProfile.run('prime(1000000)')
# 2.337 seconds

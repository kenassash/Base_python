# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
first = 5
second = 6

operator_and = first & second
operator_or = first | second
operator_xor = first ^ second

left_result = first << 2
right_result = first >> 2

print(f'{(bin(first))} и {(bin(second))}')
print(f'{bin(operator_and)}')
print(f'{bin(operator_or)}')
print(f'{bin(operator_xor)}')

print(f'{bin(left_result)}')
print(f'{bin(right_result)}')

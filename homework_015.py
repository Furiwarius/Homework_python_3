# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. F n = F n − 1 + F n − 2

from random import randrange

new_list = [0, 1]

def definition_negative(value, number):
    if number%2:return -value
    return value

for number in range(2,randrange(5, 20)):
    new_list.append(new_list[number-1]+new_list[number-2])
else:
    new_list = [definition_negative(val, n) for n, val in enumerate(new_list[:0:-1])] + new_list
print(new_list)

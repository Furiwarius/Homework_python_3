# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. F n = F n − 1 + F n − 2

from random import randrange

new_list = [0, 1]

for number in range(2,randrange(5, 20)):
    new_list.append(new_list[number-1]+new_list[number-2])
else:
    new_list = [-val for val in new_list[:0:-1]] + new_list
print(new_list)
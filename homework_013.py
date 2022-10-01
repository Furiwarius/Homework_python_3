# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части

from random import uniform, randrange

def max_fractional_difference(new_list):
    min_value = 1
    max_value = new_list[0]%1
    for val in new_list:
        val=round(val%1, 2)
        if val < min_value: min_value=val
        if val > max_value: max_value=val
    return max_value-min_value


new_list = [round(uniform(0, value), 2) for value in range(1, randrange(10,20))]
print(new_list)
print(max_fractional_difference(new_list))
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

new_list = [value for value in range(10)]
print(new_list)
bin_list = [bin(val)[2:] for val in new_list]
print(bin_list)
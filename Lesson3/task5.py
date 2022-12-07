# ; Задайте число. Составьте список чисел Фибоначчи, 
# ; в том числе для отрицательных индексов (Негафибоначчи).

number = int(input("Введите количество чисел в последовательности: "))
my_list = [0,1]
reverse_list = [0,1]

for i in range(number):
    if i>1:
        my_list.append(my_list[i-2]+(my_list[i-1]))

for i in range(number):
    if i>1:
        if (i%2) != 0:
            reverse_list.append(my_list[i-2]+(my_list[i-1]))
        else:
            reverse_list.append((my_list[i-2]+(my_list[i-1]))*-1)



print((reverse_list[::-1])+(my_list))
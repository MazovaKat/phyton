# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка с нечетными индексами.

from random import randint as rnd

size = int(input("Введите размер списка: "))
sum=0
my_list = []

for i in range(size):
    my_list.append(rnd(0,100))
print (my_list)

for i in range(len(my_list)):
    if (i%2) != 0:
        sum += int(my_list[i])
        
print (sum)

# Задайте список из n чисел последовательности (1 + 1/n)^n. 
# Вывестив консоль сам список и сумму его элементов.

number = int(input("Введите целое число: "))
sum = 0
my_list = []
for i in range(1,number+1):
    i = (1+1/i)**i
    my_list.append(i)
    sum += i

print (my_list, sum)

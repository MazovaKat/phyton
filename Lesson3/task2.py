# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = [2, 3, 4, 5, 6]
new_list = []
if len(my_list)%2 != 0 : 
    new_size = int((len(my_list)+1)/2)
    print(new_size)
    for i in range(new_size):
        new=len(my_list)-1-i
        new_list[i-1] = my_list[i] * my_list[new]
else:
    new_size = int(len(my_list)/2)
    print(new_size)
    for i in range(new_size):
        new=len(my_list)-1-i
        new_list[i-1] = my_list[i] * my_list[new]

print (new_list)

    

    




# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать!
# Реализовать свой метод

from os import remove
from random import randint as rnd

size = int(input("Введите размер списка: "))

rnd_list = []


for i in range(size):
    rnd_list.append(rnd(0,100))
print (rnd_list) 

rnd_list_new=[]
for i in range(size):
    while len(rnd_list)!=0:   
        new_element = rnd_list[rnd(i,len(rnd_list)-1)]
        rnd_list_new.append(new_element)
        rnd_list.remove(new_element)
print (rnd_list_new)

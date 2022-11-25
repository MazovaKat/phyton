# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

number_quart = int(input('Введите номер четверти (от 1 до 4):'))

if number_quart in (1,2,3,4):
    if number_quart == 1:
        print ('x>0 y>0')
    elif number_quart == 2:
        print ('x<0 y>0')
    elif number_quart == 3:
        print ('x<0 y<0')
    elif number_quart == 4:
        print ('x>0 y<0')
else:
    print ('Неверный номер четверти')
# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве

pointA_x = int(input("Введите координату Х первой точки:"))
pointA_y = int(input("Введите координату Y первой точки:"))
pointB_x = int(input("Введите координату Х второй точки:"))
pointB_y = int(input("Введите координату Y второй точки:"))

result = float(((pointB_x - pointA_x)**2 + (pointB_y - pointA_y)**2)**(0.5))
print (result) 

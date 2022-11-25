# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

my_list = [0,1]
for x in my_list:
    for y in my_list:
        for z in my_list:
            result_1 = not (x or y or z) 
            result_2 = (not x) and (not y) and (not z)
            print( x, y, z, result_1, result_2)
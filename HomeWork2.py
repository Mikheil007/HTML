# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math
spisok = list(map(int,input("Задайте список из нескольких чисел через пробел: ").split()))
print(spisok)
for i in range(len(spisok)):
     if not len(spisok) % 2 == 0:
          a = math.ceil(len(spisok)/2)
     else:
         a = len(spisok)//2
     spisok2 = []
     for j in range(a):
         spisok2.append(spisok[j] * spisok[len(spisok)-1-j])
print(f"Произведение пар чисел равно -->",spisok2)

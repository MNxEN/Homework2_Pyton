"""Задача 14: Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8"""

N = int(input("Введите число N -> "))
degree = []
i = 0
while (2 ** i) <= N:
    degree.append(2 ** i)
    i += 1
print(degree)



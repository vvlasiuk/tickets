# Найти корни квадратного уравнения

import math

def input_float(s):
    a = input(s) #  Зміній а присвоюємо значення введеної строки, користувачеві виводиться текст параметра s, після чого він вводть текст і натискає клавішу ентер.

    try:
        return float(a)
    except ValueError:
        print("isn`t number")
        quit()

print("ax2 + bx + c = 0")

a = input_float("Enter a = ")
b = input_float("Enter b = ")
c = input_float("Enter c = ")

if a == 0:
    print(" a can`t be zero")
    quit()

D = b*b - 4*a*c

print("D = " + str(D))

if D > 0:
    x1 = (-b + math.sqrt(D)) / 2*a
    x2 = (-b - math.sqrt(D)) / 2*a
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))

if D == 0:
    x = -b / 2*a
    print("x = "+ str(x))

if D < 0:
    print("Not rezult")
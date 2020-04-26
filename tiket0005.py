# Знайти площу, прямокутника, трикутника або кола. Вибір фігури обирає користувач вводом цифр 1,2,або 3

import math

def input_float(s):
    a = input(s) #  Зміній а присвоюємо значення введеної строки, користувачеві виводиться текст параметра s, після чого він вводть текст і натискає клавішу ентер.

    try:
        return float(a)
    except ValueError:
        print("isn`t number")
        quit()

x = input("Виберіть фігуру: прямокутник - 1; трикутник - 2; коло - 3: ")

if x == "1":
    a = input_float("Введіть сторону a: ")
    b = input_float("Введіть сторону b: ")
    S = a*b
    print("Площа прямокутника: " + str(S))

elif x == "2":
    a = input_float("Введіть сторону a: ")
    b = input_float("Введіть сторону b: ")
    c = input_float("Введіть сторону c: ")
    P = (a + b + c) / 2
    S = math.sqrt(P*(P-a)*(P-b)*(P-c))
    print("Площа трикутника: " + str(S))

elif x == "3":
    R = input_float("Введіть R: ")
    S = math.pi*R*R
    print("Площа круга: " + str(S))

else:
    print("Потрібно ввести тільки 1, 2 або 3")
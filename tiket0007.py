
def input_float(s):
    a = input(s) #  Зміній а присвоюємо значення введеної строки, користувачеві виводиться текст параметра s, після чого він вводть текст і натискає клавішу ентер.

    try:
        return float(a)
    except ValueError:
        print("isn`t number")
        quit()

A = input_float("Введіть сторону А = ")
B = input_float("Введіть сторону В = ")
C = input_float("Введіть сторону С = ")

if A <= 0:
    print("Сторона А повине бути більше 0")
elif B <= 0:
    print("Сторона В повине бути більше 0")
elif C <= 0:
    print("Сторона С повине бути більше 0")
else:
    if (A + B) < C:
        print("Сторона С завелика. Трикутник не може існувати.")
    elif (A + C) < B:
        print("Сторона В завелика. Трикутник не може існувати.")
    elif (B + C) < A:
        print("Сторона А завелика. Трикутник не може існувати.")
    else: print("Трикутник може існувати.")
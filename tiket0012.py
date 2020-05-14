#Перевести десятковий дріб в дріб

def str_drib(c):
    d = 0.0000000001
    b = 1
    a = 1
    y = 0
    while abs(y - a) > d:
        b = b + 1
        a = b * c
        y = int_r(a)
    a = int(a)
    return (str(a)+"/"+str(b))

def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

def input_float(s):
    c = input(s) #  Зміній а присвоюємо значення введеної строки, користувачеві виводиться текст параметра s, після чого він вводть текст і натискає клавішу ентер.

    try:
        return float(c)
    except ValueError:
        print("isn`t number")
        quit()

c = input_float("Enter numeric = ")
d = str_drib(c)

print(d)
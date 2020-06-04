#система рівнянь виду:ax + by=cdx+ey=f запитати в користувача коефіцієнти: a,b,c,d,e,fперевірити чи коєфіцієнти допустимі (ділення на 0) a,b,c,d,e,fвивести універсальну формулувикористати точність до 3 знаків після коми для х та ув кінці вивести перевирку з підставленими коефіцієнтами

def str_drib(c):
    if c == int(c):
        return int(c)

    d = 0.0000000001
    b = 0
    a = 1
    y = 0
    while abs(y - a) > d:
        b = b + 1
        a = b * c
        y = int_r(a)
    a = int_r(a)
    return str(a)+"/"+str(b)

def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

def input_float(s):
    a = input(s) #  Зміній а присвоюємо значення введеної строки, користувачеві виводиться текст параметра s, після чого він вводть текст і натискає клавішу ентер.

    try:
        return float(a)
    except ValueError:
        print("isn`t number")
        quit()

print("ax+by=c")
print("dx+ey=f")

a = input_float("Enter a = ")
b = input_float("Enter b = ")
c = input_float("Enter c = ")
d = input_float("Enter d = ")
e = input_float("Enter e = ")
f = input_float("Enter f = ")

if a == 0:
    print("Eror 1/0")
    quit()

if d == 0:
    print("Eror 1/0")
    quit()

l = b/a-e/d

if l == 0:
    print("Eror 1/0")
    quit()

y = (c/a-f/d)/l
x = (c-b*y)/a

#print("x = "+str(x))
#print("y = "+str(y))

d = str_drib(x)
h = str_drib(y)
print("x = " + str(d))
print("y = " + str(h))
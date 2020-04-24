import math
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

print("ax2 + bx + c = 0")

a = input("Enter a = ")

if not is_number(a):
    print("a isn`t number")
    quit()

b = input("Enter b = ")

if not is_number(b):
    print("b isn`t number")
    quit()

c = input("Enter c = ")

if not is_number(c):
    print("c isn`t number")
    quit()

a = float(a)
b = float(b)
c = float(c)

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
    x = -b / a
    print("x = "+ str(x))
if D < 0:
    print("Not rezult")
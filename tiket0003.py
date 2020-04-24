# Знайти значення функції

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

x = input("Enter x = ") # Зміній х присвоюємо значення введеної строки

if is_number(x): # Якщо значення змінної х є числом
    x = float(x) # Зміній х присвоюємо значення дробового числа отриманого з строки значення х

    if x == 0:
        y = 0
    elif x > 0:
        y = x - 0.5 # Зміній у присвоюємо, значення змінної х - 0.5
    elif x < 0:
        y = abs(x)
    print(y)
else:
    print("")
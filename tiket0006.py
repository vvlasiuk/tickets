#Визначити кількість днів в році, користувач вводить рік, програма видає кількість днів для даного року

def input_int(s):
    a = input(s) #  Зміній а присвоюємо значення введеної строки, користувачеві виводиться текст параметра s, після чого він вводть текст і натискає клавішу ентер.

    try:
        return int(a)
    except ValueError:
        print("Не є числом")
        quit()

y = input_int("Введіть рік: ")

if y < 0:
    print("Введіть додатній рік")
    quit()

if y%400==0:
    print("У " + str(y) + " році " "366 днів")
elif y%100==0:
    print("У " + str(y) + " році " "365 днів")
elif y%4==0:
    print("У " + str(y) + " році " "366 днів")
else:
    print("У " + str(y) + " році " "365 днів")
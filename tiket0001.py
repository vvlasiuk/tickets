#  Сума цифр введеного додатнього числа.

a = input("Enter a ")

sum = 0

if a.isdigit():
    for i in a:
        sum+=int(i)

    print(sum)
else:
    print("a isn`t int type ")
import random

a_count = 0
b_count = 0

print("Гра камінь, ножиці, папір.")
print("1 - камінь, 2 - ножиці, 3 - папір, 0 - закінчити гру")

c = ['камінь', 'ножиці', 'папір']

while True:

    b = random.choice(['0', '1', '2', '3'])

    if b == "0":
        print("Бот покинув гру")
        break

    a = input("Введіть цифру відповідну жесту: ")

    if not (a == "1" or a == "2" or a == "3" or a == "0"):
        print("Очікується введення: '1', '2', '3', '0'")
        continue

    if a == "0":
        print("Ви покинули гру")
        break

    print("Ваш хід: " + c[int(a) - 1])
    print("Хід бота: " + c[int(b) - 1])

    if a == b:
        print("Нічия")
    elif (a == "1" and b == "2") or (a == "2" and b == "3") or (a == "3" and b == "1"):
        print("Ви перемогли")
        a_count = a_count + 1
    else:
        print("Ви програли")
        b_count = b_count + 1

    print("Ваш рахунок: " + str(a_count) + " Рахунок бота: " + str(b_count))



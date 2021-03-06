import random

point = int("0")

while True:
    if point >= 50:
        print("you win!")
    a = random.randint(1, 9)
    b = input("the number is ")
    if a == b:
        print("yes! it is!")
        point = point + 1
    else:
        print("wrong!")
    print("you have %d now" %point)

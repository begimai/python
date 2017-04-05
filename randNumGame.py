import random

respond = input("Do you want to play? Enter 1 and anything else to stop ")

while int(respond) == 1:
    magic_num = random.randint(0, 99)
    var = input("Please enter number: ")
    while (int(var) != magic_num):
        if int(var) > magic_num:
            print("Too high")
        elif int(var) < magic_num:
            print("Too low")
        else:
            break
        var = input("Please enter number: ")
    print("You won!!!!! Magic number is ", magic_num)
    respond = input("Do you want to play? Enter 1 and anything else to stop ")

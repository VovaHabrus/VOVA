from random import *
import os

u_pwd = input("Введіть пароль EN and Numbers:")
pwd = ['a', 'b', 'c', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 's',
       'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'v', 'n', 'm', '1', '2',
       '3', '4', '5', '6', '7', '8', '9', '0']

pw = ""
while (pw != u_pwd):
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, 17)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("Взламування ,,, поДожі !")
        os.system("cls")
    print("Твій пароль", pw)
